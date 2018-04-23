    def __ihuan(self):
        urls = ['https://ip.ihuan.me/?page={}&anonymity=2'.format(str(i)) for i in range(1, 31)]
        for url in urls:
            for info in self.__rows_from(url):
                item = info.select('td')
                address = item[0].text + ':' + item[1].text
                if address not in self.proxies_got:
                    self.proxies_got.add(address)
            print('已采集小幻代理，代理池IP总数：', len(self.proxies_got))
   A= 人
 
Aa = 泛称 
Aa01= 人 人民 众人
Aa02= 我 我们
Aa03= 你 你们
Aa04= 他 他们
Aa05= 自己 别人 某人
Aa06= 谁
Ab = 男女老少 
Ab01= 男人 女人 男女
Ab02= 老人 成年人 老小
Ab03= 青少年
Ab04= 婴儿 儿童
Ac = 体态
Ac01= 高个子 矮子
Ac02= 胖子 瘦子
Ac03= 美女 美男子 丑八怪
Ad = 籍属
Ad01= 居民 侨民
Ad02= 本国人 外国人 外族人
Ad03= 本地人 外乡人 同乡
Ae = 职业 
Ae01= 职工 职员
Ae02= 工人
Ae03= 海员 船夫 驾驶员 搬运工
Ae04= 炊事员 伙夫
Ae05= 邮递员 门房
Ae06= 服务员 清洁工 勤杂工
Ae07= 农民 牧民 渔民
Ae08= 猎手 樵夫 饲养员
Ae09= 商人
Ae10= 军官 将士 军人 士兵
Ae11= 情报员
Ae12= 警察 审判员 律师
Ae13= 教师 学生
Ae14= 运动员 裁判员
Ae15= 医生 护士 助产士
Ae16= 作者 译者 记者 编辑
Ae17= 演员 琴师 剧团人员
Ae18= 阴阳家 巫师
Af = 身份 
Af01= 劳动者 奴隶 小市民
Af02= 仆人 仆从
Af03= 封建主 地主 士绅
Af04= 资本家
Af05= 皇帝 后妃
Af06= 皇室 王公 贵族
Af07= 太监 宫女 女官
Af08= 官吏
Af09= 宰相 幕宾 门客 使者 
Af10= 领袖 领导
Af11= 名人 隐士 小人物
Ag = 状况 
Ag01= 健康人 病人 疯子
Ag02= 伤员 餐费 孕妇
Ag03= 鳏寡孤独
Ag04= 富翁 穷人
Ag05= 幸运儿 红人
Ag06= 可怜虫 瓮中之鳖 众矢之的
Ag07= 屈死鬼 被害人 冤大头 祸胎
Ag08= 难民 灾民 流亡者 流浪汉
Ag09= 败兵 俘虏
Ag10= 旅客
Ah = 亲人 眷属
Ah01= 亲戚 眷属
Ah02= 曾祖 祖父 祖母
Ah03= 伯祖 叔祖 外祖父 外祖母
Ah04= 父 母 父母 父子
Ah05= 伯父 伯母 叔父 叔母
Ah06= 姑父 姑母 姨父 姨母 舅父 舅母
Ah07= 公婆 岳父 岳母
Ah08= 夫 妻 夫妻
Ah09= 兄 弟 兄弟
Ah10= 姐 妹 姐妹
Ah11= 妯娌 连襟
Ah12= 嫂子 弟媳 姐夫 妹夫
Ah13= 妻舅 姑 姨
Ah14= 子 女 子女
Ah15= 媳妇 女婿 翁婿
Ah16= 侄子 外甥
Ah17= 孙
Ai = 辈分
Ai01= 鼻祖 前辈 今人 后人
Ai02= 祖宗 长辈
Ai03= 同辈 晚辈 子孙 
Aj = 关系 
Aj01= 朋友 恩人 仇人 对手
Aj02= 自己人 外人 邻居
Aj03= 一伙 同伴 把兄弟
Aj04= 同事 同学
Aj05= 主人 客人 宾主
Aj06= 顾客
Aj07= 成员
Aj08= 上级 下级 平级
Aj09= 助手 参谋 靠山
Aj10= 师傅 徒弟
Aj11= 物主
Aj12= 主持人 司仪 与会者
Aj13= 专人 代表
Aj14= 见证人 保证人 中间人 调解人 仲裁者
Aj15= 介绍人 媒人 傧相
Aj16= 新娘 新郎
Aj17= 情人 姘头 王八
Ak = 品性 
Ak01= 英雄 硬汉 烈士
Ak02= 勇士 侠客 懦夫 懒汉
Ak03= 好人 君子 圣贤 坏人 
Ak04= 老好人 凶人
Ak05= 伪君子 滑头
Ak06= 吝啬鬼 市侩
Ak07= 孝子 逆子
Ak08= 烈女 荡妇 
Ak09= 浪子 色鬼
Ak10= 老顽固 学究
Ak11= 急性子 慢郎中
Ak12= 话匣子 应声虫 馋嘴 夜游神 怪人
Al = 才识 
Al01= 知识分子 文盲
Al02= 内行 专家 骨干 外行
Al03= 俊杰 人才
Al04= 聪明人 笨伯
Al05= 模范 先锋 功臣
Al06= 爱好者
Am = 信仰 
Am01= 教徒 佛教徒
Am02= 道教徒 
Am03= 伊斯兰教徒 天主教徒 基督教徒
An = 丑类
An01= 反动派 叛徒
An02= 罪犯
An03= 强盗 窃贼
An04= 流氓 骗子 投机商
An05= 走狗
An06= 赌徒 酒鬼 烟鬼
An07= 妓 娼 娼妓 嫖客
B= 物
Ba= 统称
Ba01= 物 物体
Ba02= 生物
Ba03= 物品 物件
Ba04= 货物 产品
Ba05= 器具 设备
Ba06= 物资 生活资料
Ba07= 礼品 嫁妆 祭品
Ba08= 宝物 废物 
Ba09= 担子 包裹
Ba10= 它 什么
Bb= 拟状物
Bb01= 锭 块
Bb02= 粉 点 粒
Bb03= 堆 把
Bb04= 球 片 筒
Bb05= 捧
Bb06= 网 波
Bc= 局部
Bc01= 顶 底
Bc02= 边 角 面 脊
Bc03= 身 颈 弯子 骨架
Bc04= 盖 杆 柄
Bc05= 嘴 座 脚 翼 挡 心

Bd= 天体
Ba01= 宇宙 星辰
Ba02= 太阳 月亮 日月
Ba03= 地球
Be= 地貌
Be01= 陆地 原野 沙漠
Be02= 岛屿 沙洲
Be03= 滩 岸
Be04= 山 坡
Be05= 海洋 江河 溪涧
Be06= 湖泊 池塘 泥坑
Be07= 泉水 瀑布
Be08= 遗迹 废墟
Bf= 气象
Bf01= 雨 雪 冰 雹
Bf02= 风 云
Bf03= 露 霜
Bf04= 虹 霞
Bf05= 烟 雾 霾
Bf06= 雷 闪电
Bf07= 潮汛
Bg= 自然物
Bg01= 水 汁 浆
Bg02= 泡 波浪
Bg03= 火 光 影
Bg04= 电 电波
Bg05= 气
Bg06= 颜色 气息 味道
Bg07= 声音 音调 节拍
Bg08= 灰尘 污垢
Bg09= 纹路 痕迹
Bh= 植物
Bh01= 树木 竹
Bh02= 花 花卉
Bh03= 草
Bh04= 藻 苔藓 菌菇
Bh05= 五谷
Bh06= 蔬菜
Bh07= 水果
Bh08= 草药
Bh09= 经济作物
Bh10= 植株 茎 枝
Bh11= 根 叶 花朵
Bh12= 芽 苗 柄 蒂
Bh13= 果实 种子
Bi= 动物
Bi01= 牲畜 野兽
Bi02= 狮 虎 豹 象 猛犸
Bi03= 熊 狼 狐
Bi04= 猿猴
Bi05= 鹿 獐 骆驼
Bi06= 驴 马 牛 羊
Bi07= 猪 狗 兔
Bi08= 猫 鼠
Bi09= 鳄鱼 鲸 海豚 江豚 人鱼
Bi10= 蛇 蛙 蜥蜴 獭
Bi11= 禽兽 禽
Bi12= 鹰 雀 鸽 鹤 鸥
Bi13= 鸡 鸭 鹅
Bi14= 鱼 鱼虾
Bi15= 龟 鳖
Bi16= 虾 蟹 蚌 螺
Bi17= 海参 鲍鱼 海蜇
Bi18= 昆虫
Bi19= 蜂 蚕
Bi20= 蝶 蛾 蜘蛛
Bi21= 蝗虫 螟虫 蚜虫
Bi22= 蚊 蝇 蚁
Bi23= 臭虫 跳蚤 水蚤 虱
Bj= 微生物
Bj01= 细菌 病菌
Bj02= 酵母菌 霉菌
Bk= 全身
Bk01= 身体 尸体
Bk02= 头 脸 脑
Bk03= 眼 耳 鼻
Bk04= 口 牙 齿
Bk05= 颈 肩 胸 乳房
Bk06= 背 腰
Bk07= 腹 臀
Bk08= 四肢 手 臂 腿 脚
Bk09= 角 触角 尾 鳍 翼
Bk10= 皮肤 肌肉
Bk11= 毛 发
Bk12= 眉毛 睫毛 胡须
Bk13= 骨骼 指甲 甲壳 鳞
Bk14= 内脏 心 肺 胃 肠
Bk15= 生殖器 胎
Bk16= 经络 骨髓 神经
Bk17= 腺 膜
Bk18= 血液 淋巴
Bl= 排泄物 分泌物
Bl01= 汗 痰 奶水
Bl02= 体液 月经
Bl03= 眼泪 鼻涕 耳屎 眼屎 头皮屑
Bl04= 屎 尿
Bl05= 精液 卵
Bm= 材料
Bm01= 五金 金 银 铜
Bm02= 钢 铁
Bm03= 木料 软木
Bm04= 土 石 泥 沙
Bm05= 水泥 石灰 沥青
Bm06= 砖 瓦
Bm07= 板 管
Bm08= 煤 炭
Bm09= 木柴 火煤 松明 灯油
Bm10= 石油 酒精 润滑油 煤油
Bm11= 颜料 染料 油漆
Bm12= 蚕丝 棉纱 化学纤维
Bm13= 皮革 毛皮
Bm14= 胶
Bm15= 陶瓷 玻璃
Bm16= 珍珠 玉石 象牙 琥珀 钻石
Bm17= 赛璐璐 搪瓷 电木
Bm18= 肥料



Bn= 建筑物
Bn01= 建筑 房屋
Bn02= 别墅 公馆
Bn03= 房间
Bn04= 门 窗 门窗
Bn05= 地基 地面 天花板
Bn06= 梁 柱 桩
Bn07= 墙壁 篱笆 栅栏
Bn08= 屋檐 排水沟
Bn09= 阳台 院子
Bn10= 走廊 台阶 楼梯 栏杆
Bn11= 路 胡同 桥 巷
Bn12= 田地 田埂 园圃 温室 苗床
Bn13= 圈 笼 窠 陷阱
Bn14= 书库 堤坝 水闸
Bn15= 沟渠 井
Bn16= 矿井 坑道 工作面
Bn17= 发电站 仓库
Bn18= 营房 堡垒 烽火台
Bn19= 掩体 壕沟
Bn20= 园林
Bn21= 塔 亭 阁 台
Bn22= 坟墓 墓穴 碑
Bn23= 皇宫 祠堂 佛殿
Bn24= 庙宇 清真寺 教堂
Bo= 机具
Bo01= 机具 工具 泵
Bo02= 机床 刀具
Bo03= 机件
Bo04= 通信器材 电线 电料
Bo05= 农具 渔具
Bo06= 磨子 锥
Bo07= 蚕箔 蚕蔟
Bo08= 工匠用具
Bo09= 剪 刀 斧 刃
Bo10= 锤 镐 凿 锹 铲
Bo11= 刨 锯 锉
Bo12= 钳 钻 改锥
Bo13= 棒 杠
Bo14= 墩子 砧板
Bo15= 模具 楦子
Bo16= 夹具 榫头
Bo17= 版
Bo18= 仪表 量具 称 斗
Bo19= 炉
Bo20= 医疗防护器材
Bo21= 车
Bo22= 船 筏子 飞机
Bo23= 轿子 雪橇
Bo24= 舵 桨 帆 桅杆 舱
Bo25= 车把 方向盘 车轮 轮胎
Bo26= 辔头 马掌 鞭子 马鞍
Bo27= 武器 枪 炮 刺刀
Bo28= 弹药 炸药
Bo29= 弓 箭 矛 盾 刀 剑
Bo30= 军舰 战斗机 坦克
Bo31= 火箭 导弹
Bo32= 赌具 烟具 刑具
Bp= 用品
Bp01= 灯 镜子 眼镜
Bp02= 刷 扫帚 拖把
Bp03= 毛巾 肥皂 梳子
Bp04= 针 线 针线
Bp05= 锅 壶 蒸笼 勺 筷子
Bp06= 盆 桶 瓶
Bp07= 盘 杯 碗
Bp08= 坛子 罐子 缸
Bp09= 箱 盒
Bp10= 篮 篓 笼 箩筐 簸箕
Bp11= 包 袋 套
Bp12= 体育用品 球 棋
Bp13= 乐器
Bp14= 幕 布景
Bp15= 相机 胶片
Bp16= 文具
Bp17= 笔 墨 纸 砚
Bp18= 卡片 名帖 簿册
Bp19= 单据 证书 凭证
Bp20= 标志 旗帜
Bp21= 图章 徽章
Bp22= 香 蜡烛 香烛
Bp23= 火柴 火把
Bp24= 纽扣 结
Bp25= 绳 链 带
Bp26= 桌子 抽屉 椅子 凳子
Bp27= 床 橱 屏风
Bp28= 卧具 被褥 毯子 枕头 床单
Bp29= 帐子 席子 帘 帐幕
Bp30= 垫子 罩子
Bp31= 钟 表
Bp32= 化妆品
Bp33= 饰物 首饰 针织品
Bp34= 伞 扇子 取暖器
Bp35= 玩具
Bp36= 响器 花炮
Bp37= 棺材 冥器
Bq= 衣物
Bq01= 衣 布 绒
Bq02= 丝绸 呢绒
Bq03= 衣服 上装 裤子 裙
Bq04= 领子 裤腰 口袋 袖子 衣襟
Bq05= 鞋 帽 靴
Bq06= 头巾 围巾 袜
Br= 食品 药品 毒品
Br01= 粮食
Br02= 饲料 粮草 鱼饵
Br03= 食物
Br04= 饭 粥 锅巴
Br05= 面食 杂粮
Br06= 菜肴 荤菜 素菜
Br07= 调味品
Br08= 油 盐 酱 醋 糖
Br09= 点心
Br10= 糖果 蜜饯
Br11= 果料 馅料 酵母
Br12= 饮料 茶 酒 乳酪
Br13= 药片 维生素 补品
Br14= 毒品 鸦片 砒霜 烟
C= 时空
Ca= 时间
Bp01= 阳历 阴历 公元
Bp02= 时代 年代 朝代
Bp03= 毛巾 肥皂 梳子
Bp04= 针 线 针线
Bp05= 锅 壶 蒸笼 勺 筷子
Bp06= 盆 桶 瓶
Bp07= 盘 杯 碗
Bp08= 坛子 罐子 缸
Bp09= 箱 盒
Bp10= 篮 篓 笼 箩筐 簸箕
Bp11= 包 袋 套
Bp12= 体育用品 球 棋
Bp13= 乐器
Bp14= 幕 布景
Bp15= 相机 胶片
Bp16= 文具
Bp17= 笔 墨 纸 砚
Bp18= 卡片 名帖 簿册
Bp19= 单据 证书 凭证
Bp20= 标志 旗帜
Bp21= 图章 徽章
Bp22= 香 蜡烛 香烛
Bp23= 火柴 火把
Bp24= 纽扣 结
Bp25= 绳 链 带
Bp26= 桌子 抽屉 椅子 凳子
Bp27= 床 橱 屏风
Bp28= 卧具 被褥 毯子 枕头 床单
Bp29= 帐子 席子 帘 帐幕
Bp30= 垫子 罩子
Bp31= 钟 表
Cb= 空间
D= 抽象事物
Da= 事情 情况
Db= 事理
Dc= 外貌
Dd= 性能
De= 性格 才能
Df= 意识
Dg= 比喻物
Dh= 意想物
Di= 社会 政法
Dj= 经济
Dk= 文教
Dl= 疾病
Dm= 机构
Dn= 数量 单位
E= 特征
Da= 外形
Da= 表象
