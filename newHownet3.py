# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 参考2017年10月最新论文，改善在知网上计算相似度的质量。
@DateTime: Created on 2018/2/27, at 下午 04:57 by PyCharm '''


class GlossaryElement:
    '''    #词汇表条目    '''

    def __init__(self):
        self.word = ''  # 词
        self.type = ''  # 词性
        self.solid = False  # 实词/虚词
        self.s_first = ''  # 第一基本义原
        self.s_other = []  # 其他义原
        self.s_relation = {}  # 关系义原
        self.s_symbol = {}  # 符号义原

    def dump(self):
        print(self.word + ',' + self.type + ', | first:' + self.s_first + ' | other:')
        for i in range(len(self.s_other)):
            print(self.s_other[i] + ',')

        print(' | relation:')
        for it in self.s_relation.keys():
            print(it + '=' + self.s_relation[it] + ',')

        print(' | symbol:')
        for it in self.s_symbol.keys():
            print(it + '=' + self.s_symbol[it] + ',')

        print('\n')

    def parse(self, text):
        line = text
        if not line.strip():  # 如果本行为空，则返回False。不为空，则进行解析
            return False
        items = line.split('/')
        if len(items) == 3:
            self.word = items[0]
            self.type = items[1]
            if line[0] != '{':
                self.solid = True
            else:
                self.solid = False
                line = line[1:len(line) - 2]

            sememes = items[2].split(',')

            if len(sememes) > 0:
                firstdone = False
                if sememes[0][0].isalpha():  # 如果义原是字母开头，那么提取第一级别义原
                    self.s_first, defaultText = parseZhAndEn(sememes[0])
                    firstdone = True

                for i in range(len(sememes)):
                    if 0 == i and firstdone:  # 如果提取到了第1义原，则跳过第0次处理。
                        continue

                    firstletter = sememes[i][0]
                    if '(' == firstletter:  # 其他义原解析
                        self.s_other.append(sememes[i])
                        continue
                    equalpos = sememes[i].find('=')
                    if equalpos != -1:  # 关系义原解析
                        key = sememes[i][0:equalpos]
                        value = sememes[i][equalpos + 1]
                        if len(value) > 0 and value[0] != '(':
                            value, defaultText = parseZhAndEn(value)
                        self.s_relation[key] = value
                        continue

                    if not firstletter.isalpha():  # 符号义原解析
                        value = sememes[i][1:]
                        if len(value) > 0 and value[0] != '(':
                            value, defaultText = parseZhAndEn(value)
                        self.s_symbol[firstletter] = value
                        continue
                    self.s_other.append(sememes[i])
            # self.dump()
            return True
        return False

    def make_formula(self, line):
        if not line.strip():  # 如果本行为空，则返回False。不为空，则进行解析
            return set()
        items = line.split('/')
        if len(items) == 3:
            self.word = items[0]
            sememes = items[2].strip().replace('^', '').replace('~', '').split(',')  # 后面是义原表达式
            relation = ['#', '%', '$', '*', '+', '&', '@', '?', '!']
            formula, num = '', 0
            for yiyuan in sememes:
                if yiyuan[0] in relation:  # 如果是符号义原表达式，把开头符号去掉
                    formula += '∩'
                    formula += yiyuan[1:]
                    num += 1
                elif yiyuan.find('=') > -1:  # 如果是关系义原表达式，只提取 = 后的义原。
                    formula += '∩'
                    formula += yiyuan.split('=')[-1]
                    num += 1
                elif yiyuan.endswith('}'):  # 对于虚词，提取大括号内的部分。肯定是独立义原而且唯一。
                    formula = yiyuan[1:-1]
                    num += 1
                elif yiyuan[0].isalpha():  # 如果独立义原不是第一个，添加一个∪符号。
                    if num > 0:
                        formula += '∪'
                    formula += yiyuan
                    num += 1
            # 对形成的表达式切分，划分为单个的表达式组成列表
            form_list = formula.split('∪')
            return set(form_list)
        return set()


class SememeElement:
    '''    义原条目    '''

    def __init__(self):
        self.id = '-1'  # 编号
        self.father = []  # 父义原编号
        self.sememe_zh = ''  # 中文义原，中间的en|zh名称。

    def parse(self, line):
        if not line:  # 如果当前行为空，不解析，返回False
            return False
        items = line.split()
        if len(items) == 3:
            self.id = items[0].strip()
            self.sememe_zh = items[1].strip()
            self.father.append(items[2].strip())
            return True
        return False

    def __str__(self):
        full = self.id + self.sememe_zh
        for fa in self.father:
            full += fa
            full += ','
        return full


def valuesOfGlossarytable_(glossarytable_, word):
    values_ = []
    for key_, v_ in glossarytable_.items():
        key_ = key_.split('\t')[1]
        if key_ == word:
            values_.append(v_)
    return values_


class How_Similarity:

    def __init__(self):
        self.sememetable_ = dict()  # 义原表,从id找到义原对象。
        self.sememeindex_zn_ = dict()  # 义原索引(中文)，根据中文词找到义原。
        self.glossarytable_ = dict()  # 词汇表。
        self.glossaryfile = './hownet/glossary.txt'
        self.sememefile = './hownet/whole.dat'
        self.full_set = set()  # 所有出现过的义原集合。
        self.vocab = set()
        self.form_dict = {}  # 单词到表达式的字典
        self.all_fathers = []
        self.begin = 2000
        # self.init()

    def init(self):
        '''        初始化义原和词汇表        '''
        if self.loadSememeTable(self.sememefile) == False:
            print("[ERROR] %s 加载失败.", self.sememefile)
            return False
        if self.loadFormula() == False:
            print("[ERROR] %s 加载失败.", self.glossaryfile)
            return False
        return True

    def loadSememeTable(self, filename):
        with open(filename, 'rt', encoding='utf-8') as reader:
            try:
                lines = reader.readlines()
                for line in lines:
                    ele = SememeElement()
                    if not ele.parse(line):  # 如果当前行为空，迭代下一行
                        continue
                    if ele.sememe_zh in self.sememeindex_zn_.keys():  # 如果义原出现过。id不变，只添加父节点
                        self.sememeindex_zn_[ele.sememe_zh].father += ele.father
                    else:
                        self.sememetable_[ele.id] = ele  # 如果是全新节点。则加入到id索引表。和字面名索引表。
                        self.sememeindex_zn_[ele.sememe_zh] = ele
            except Exception as e:
                print('function loadSememeTable has Errors!!')
                print(e)
                return False
        return True

    def loadFormula(self):
        '''        加载全部表达式        '''
        with open('ZW0301.txt', 'r', encoding='utf-8') as reader:
            try:
                lines = reader.readlines()
                if not lines:  # 从 lines = [] 改为 not，更pythonic
                    return False
                for line in lines:
                    if not line.strip():  # empty函数 == False 改得更pythonic。
                        continue  # 使用continue，减小嵌套深度
                    ele = GlossaryElement()
                    forms = ele.make_formula(line)
                    if forms:
                        self.vocab.add(ele.word)
                        if ele.word in self.form_dict.keys():
                            self.form_dict[ele.word].update(forms)  # 如果该词出现过，将列表追加到末尾。
                        else:
                            self.form_dict[ele.word] = forms  # 如果词第一次出现，直接赋值。
                    self.full_set.update(forms)
                    #  print('function loadGlossary has been completed!!')
            except Exception as e:
                print('function loadFormula has errors!!', e)
                return False
            # 对每个不重复单词，肯定要增加一个义原节点对象。分配编号。
            # 只有义项、概念全部建立之后，再为每个词、概念，递归地设置父节点id。


        self.add_to_table(self.full_set)
        self.add_to_table(self.vocab)
        return True

    def add_to_table(self, things):
        for sememe in things:  # 对每个概念，判断是否在义原table中存在，如果存在，则不创建新义原对象。
            # 否则建立对象，分配编号。依次顺延。
            if sememe in self.sememeindex_zn_.keys():
                continue
            ele = SememeElement()  # 父节点留待后面设置。
            ele.id = str(self.begin)
            self.sememetable_[ele.id] = ele
            ele.sememe_zh = sememe
            self.sememeindex_zn_[sememe] = ele  # 根据概念式本身找到义原对象。
            self.begin += 1

    def give_fathers(self):
        # 对于单词来说，直接挂在可以查询到的概念上即可。单词存在多重继承，用列表形式。多个父亲id可以用 / 分隔。
        for word, express in self.form_dict.items():
            self.sememeindex_zn_[word].father = []
            for sem in express:  # epress 是单词对应的基本义原、抽象概念的集合。
                self.sememeindex_zn_[word].father.append(self.sememeindex_zn_[sem].id)
        print('所有单词挂钩到对应概念完成!')  # 完成这一步说明所有出现过的概念，无论基本还是抽象，都可以找到自己的id。
        count = 0
        for concept in list(self.full_set):
            if len(concept.split('∩')) <= 1:  # 对于表达式中的概念，如果按'∩'分割长度为1，基本义原不做处理。
                count += 1
                # print('第{}概念：{}直接跳过!'.format(count, concept))  # 基本义原已经有了父节点。
                continue
            else:
                base = concept[:concept.rfind('∩')]  # 减去末尾一个约束条件，判断是否存在
                while base not in self.sememeindex_zn_.keys():
                    pos = base.rfind('∩')
                    if pos > 0:
                        base = base[:pos]  # 如果不存在，再减去末尾一个约束条件，直到base存在为止。
                    else:
                        break
                count += 1
                # print('第{}概念：{}挂钩到义项树{}完成!'.format(count,concept,base))
                self.sememeindex_zn_[concept].father = self.sememeindex_zn_[base].id  # 原始概念的父概念设置为基本概念。
        print('所有概念挂钩到义项树完成!')

    def my_father(self, word_index):
        # # 给过来的应该是索引号。这样方便用父节点的索引号递归。
        if '0' == word_index or self.sememetable_[word_index].father[0] == word_index:
            return
        fa_list = self.sememetable_[word_index].father
        self.all_fathers += fa_list
        for one in fa_list:
            self.my_father(one)

    def get_ancestors(self, word):
        index = self.sememeindex_zn_[word].id
        print('该词索引号：', index, type(index))
        self.my_father(index)
        return set(self.all_fathers)

    def common_Father(self, w1, w2):
        A, B = self.get_ancestors(w1), self.get_ancestors(w2)
        in_common = list(A & B)
        print(A,B,in_common,sep='\n')
        common = [int(a) for a in in_common]  # 转换为数字的list
        order = sorted(common)
        return str(order[-1])  # 返回数据值最大的公共祖先。就是最近公共概念。

    def depth_of(self, concept):
        '''给定一个概念，获得其深度。路径是唯一的。
           给定一个单词。因为有多条路径通往根节点，路径不唯一。深度取最小值？
           给每个单词/概念标注深度。执行策略：
           1，对于father就是自己的节点，深度为0。这些节点组成listA
           2，如果节点已有深度值，跳过。father列表中只要任何一个in listA，那么深度为1。这些深度为1的节点组成listB
           3，依次类推，就可以标注完全部节点的最小深度。【因为从上到下梳理，先得到的深度必然最小。】
           最后获取深度只需要查表就行了。
        :param concept: 概念名
        :return: 概念在义项网中的层数，顶层为0，最深可能是17。
        '''
        pass

    def hypo_num(self, concept):
        '''【广度优先】
        1，先遍历一遍，找到father==它的直接下位节点清单。
        2，然后对每个下位节点，找它的直接下位节点清单。
        3，直到所有子节点没有下位元素为止。
        4，统计不重复子节点的总数量。
        :param concept: 概念名
        :return: 所有孩子节点总数。最小为0，最大可能是6万多。
        '''
        pass


if __name__ == '__main__':
    aa = How_Similarity()
    aa.loadSememeTable('whole.dat')
    aa.loadFormula()
    aa.give_fathers()


    # for ele in aa.sememeindex_zn_.values():
    #     print(ele.id, ele.sememe_zh, ele.father, )

    fa = aa.common_Father('楼房','工地')
    print('公共父节点是：',fa,aa.sememetable_[fa].sememe_zh)
    #

    print('词条总数', len(aa.form_dict), '词义中出现的不重复概念总数：', len(aa.full_set))
    print('全部节点数：{}'.format(len(aa.sememetable_)))
    print('全部节点数：{}'.format(len(aa.sememeindex_zn_)))
