import re
from utils import safe_add

new_vcs = ["北京泽一投资", "巨人网络(巨人创投)", "紫辉创投", "英诺天使基金", "泰岳梧桐资本", "明势资本", "真顺基金", "唯品会", "Star VC", "微纳点石", "Lightbox Ventures", "网信集团", "Aspect Ventures", "云溪投资", "梅花创投", "承珞资本", "天神娱乐", "暾澜投资", "BWVC泽厚资本", "H Capital", "中凌晟银", "科创集团(上海科创)", "线性资本", "源码资本", "志成资本", "云启资本", "蓝湖资本", "弘晖资本", "无穹创投", "恒泰资本CHT Capital", "暴龙资本", "乐顺创投", "伯藜创投", "瀚霖资本", "小马蜂创投", "洪泰基金", "伙伴创投", "联想创投集团", "以太创服（以太资本）", "博派资本", "同渡资本", "京北投资", "湖畔山南资本", "黑马基金", "元璟资本", "正和岛正和磁系资本", "陶石资本", "德沃基金", "光信资本", "光华弘人资本", "哈鲁资本", "众海投资", "执一资本", "创享投资", "考拉资本", "基因资本", "进化资本", "浅石创投", "熊猫资本", "唯猎资本", "长石资本", "微光创投", "崭越资本", "迭代资本", "曲速创投", "熙金资本", "愉悦资本", "峰谷资本", "七海资本", "挚盈资本", "乾明投资", "澜哲资本", "火柴快鹿投资基金", "远翼投资", "大河创投", "动域资本", "嵩山资本", "洋葱基金", "光源资本", "蝙蝠资本", "星瀚资本", "风云资本", "逐鹿资本", "AB资本-AB Capital", "全明星投资All-Stars Investment", "分布式资本", "初心资本", "飞鱼科技", "是成资本", "正时资本", "春晓资本", "和璞资本", "晨晖资本", "疆域资本", "湾海投资", "零一创投", "蓝象资本", "天使汇", "琢石投资", "杭州多牛资本", "英雄互娱", "狮享家新媒体基金", "众诚资本", "峰瑞资本", "高维资本", "青骢资本", "华泽资本", "蚂蚁金服(阿里巴巴)", "春风创投(春雨医生)", "国金投资", "耀途资本", "济峰资本", "MFund魔量基金", "创势资本", "箭速资本", "黑桃资本", "红谷资本", "AA投资", "泰有投资", "紫牛基金", "乾彭资本", "知初资本", "中科创星", "华兴新经济基金", "丰实资本", "中科乐创", "优客工场", "众为资本", "辰海资本", "火石资本", "周大福VMS Legend Investment", "三行资本", "集结号资本", "稻谷资本", "黑洞投资", "海泉基金(胡海泉)", "梧桐理想资本", "高樟资本", "徽瑾创投", "十方创投", "常见投资（本见投资）", "中沃投资", "青锐创投", "道生资本", "左驭资本", "孝昌水木投资", "探针创投", "中金汇财投资", "微影资本(微影时代)", "道彤投资", "春泉创投", "见证投资", "浙商产融", "清华x-lab创业DNA基金", "山谷资本", "乐尧创投", "安持资本", "明嘉资本", "臻云创投", "和悦资本", "March Capital", "元生资本", "明道资本", "创大资本", "墨白资本", "凡卓资本(小饭桌)", "尚势资本", "集素资本", "绩优投资", "寒武创投", "韬蕴资本", "天善资本", "头头是道投资基金", "方信资本", "康桥资本", "通和毓承", "峰尚资本", "晨曜资本(晨之科)", "光大体育文化投资基金", "星沅空间", "冠军VC", "考拉基金(拉卡拉)", "金复资本", "岚源资本", "莲花资本", "金砖资本", "玖创资本", "长江产业基金", "斑马资本", "青桐资本", "中金甲子", "前海梧桐并购基金", "鼎祥资本", "云椿资本", "唯嘉资本", "喜乐佳投资", "西部资本", "尚珹资本", "雅瑞资本", "阳光融汇资本", "众乐投资", "指数资本", "景峰医药(康景资本)", "启嘉创投", "能图资本", "佳浩投资", "穆棉资本", "如川投资", "齐一资本", "云起资本", "盛山资产", "AC加速器", "松禾远望", "元航资本", "领医创造", "深圳中韩产业投资基金", "合一资本", "英谊资本", "稼沃资本", "海贝同创", "恺富资本", "芒果文创基金", "澎湃资本", "千乘资本", "EMC媒体基金", "新浚资本", "云九资本", "黑蝶资本", "众善创投", "宜信财富", "前海梦创", "天时开元", "绿地润东汽车", "华兴Alpha", "阿里巴巴创业者基金", "大鹏航服", "云和资本(云和方圆)", "投控东海投资", "火橙资本", "富涌谷资本", "文徽投资", "合福资本(景瑞控股)", "伯恩资本", "阿里体育(阿里巴巴)", "璘晖创投", "正心谷创新资本", "万家朴智(万家基金)", "预鉴资本", "洪晟观通基金", "沃肯资本", "华仰投资", "赛航基金", "竞远投资", "保利资本", "前海勤智资本", "前海母基金", "中鸿嘉资本", "上海复容投资", "贝格控股", "猎鹰创投", "涟漪投资", "SuperG速普创投", "百纳资本", "上海越银投资", "新龙脉控股", "卡氏中国基金", "以正资本", "点石资本", "雪杉基金", "复之硕资本-安硕信息", "前海杰维资本", "金科君创", "We+母基金", "雨和资本", "本草资本", "洪城资本", "中舒投资", "黑蚁资本", "幂方资本", "创见资本", "武汉众合创投资", "非同凡想创投", "华信资本", "德屹资本", "君上资本", "东合资本", "独秀资本", "元和资本", "深圳金坤投资", "高林资本", "同人博达", "为润资本", "中青创投", "Alliance Capital同人融资", "远望资本", "广东温度创投", "深圳城蓝资产", "德高广宇", "趵朴投资", "赛智创投", "百度资本", "苏州清研资本", "光际资本(IDG-光大)", "绿领资本", "头狼资本-头狼金服", "创创基金", "复朴投资", "盛世方舟", "春晖资本", "1898创投", "若沐资本", "氧气资本", "泉创资本", "牛润创投", "索道投资", "同禾资本", "和暄资本Hermitage Capital", "锐旗资本", "禾今投资", "鑫丘投资", "机智股权投资", "一号公路资本", "厦门庆年投资", "建元基金", "昆仲资本", "博嵩资本", "IMO Ventures", "云和资本", "上海中悉投资", "创徒丛林-创徒投资", "国都创投(国都证券)", "Jeneration Capital时代资本", "领势投资", "英大资本", "原链资本", "源星图创投", "科鑫资本", "前海长城基金", "上海近业投资", "云禾资本", "北京生活性服务业基金", "元晓资本", "杭州驷腾投资", "九吾医疗投资", "杭州多融创投", "华众沃赋", "香樟投资", "伙星人投资", "领投会中国投资人中心", "中民投", "乾然资本", "清科母基金", "创世资本", "融磊资本", "国际创投", "福鱼资本", "甬港无咖投资", "四川文化产业股权投资基金", "曜为资本", "光控众盈资本", "红石先锋", "华业天成(华诺创投)", "中启资本", "杭州秘银资本", "SMG上海文广", "钱塘体育文化基金", "北广文资歌华基金", "马良资本", "中电健康基金", "元气资本", "中原资产(中原股权投资)", "拉芳投资", "明照资本", "厦门拉隆基金", "国投东兴", "赛苏投资", "御风资本", "儒者创投", "绝了基金", "淳元资本", "爱奇艺", "国盛金控(华声股份)", "番茄资本", "猫眼资本", "嘉实投资-嘉实基金", "天使百人会", "蓝杉创投", "汇鼎医疗投资", "大航海基金", "润良泰基金", "竑观投资", "昆通投资", "嘉远基金", "晨山资本", "胖猫创投(找钢网)", "恒兴资本", "珞珈创新天使基金", "联石投资", "弘治资本", "盈正投资", "金艮集团", "中金启元", "元创资本", "桃李创投", "华夏桃李资本", "宽象资本", "乾盛乾资本", "光远资本", "原创资本", "杭州璞程投资", "拾玉资本", "润浙资本", "君和资本", "未然资本", "授羽投资", "链动投资-科达股份", "国家中小企业发展基金（国中创投）", "富通德宝", "易合资本", "创金资本", "钜融产业基金", "JadeValue", "谷银基金", "108度资本", "FutureX Capital天际资本", "天际资本", "汇盈博润", "三峡资本", "十分咖啡-十分资本", "厦门弘雅资本", "青瓦资本", "辰韬资本", "众源资本", "启宸资本", "银河系创投", "乐有投资", "襄禾资本", "兴旺投资", "挚金资本", "千山资本", "愿景资本", "新动金鼎体育基金", "火山石资本", "Blue Pool Capital(阿里巴巴)", "中国国有资本风险投资基金（国风投基金）", "宜华资本", "点亮基金", "沸点资本", "尼莫创投", "名川资本", "品清资本", "德众资本", "将门创投", "醒澜投资", "红点创投中国基金", "百润央银", "水木资本", "威资顿资本", "铂欣资本", "清源联创", "翰同资本", "通衡浙商资本", "红筹投资", "翊翎资本", "LDV Partners复盛创投", "国宏嘉信", "君同资本", "一村资本", "光亮资本", "松柏资本", "InteBridge英智资本", "东玖汇集团开易资本", "东玖资本", "海通新创投资", "海朋资本", "合享资本", "CCiC文创孵化中心", "长岭资本", "易科汇资本", "知新资本", "诚存资本", "毅聪创投", "拙朴投资", "磐丰投资", "港粤资本", "壹号资本", "黄浦江资本", "大营资本", "伽利略资本", "0331创投", "浩方创投", "聚创造", "丰年资本", "金昌投资", "信元资本", "骑士创投", "律格资本", "白马资本", "引爆点资本", "沣源资本", "庆峰基金", "腾股创投", "启道创投", "健盛体育专项基金", "比由技术工场", "追远创投", "健桥资本", "极豆资本", "方和资本", "中科创客学院", "志拙资本", "创世伙伴资本", "厚扬投资", "本翼资本", "契阔资本", "中骏资本", "洪泰智造工场", "轻舟资本", "健禧投资", "首建投资本", "怀记投资", "蛋壳投资(动脉网)", "万美资本", "奋毅资本", "昂若资本", "苏美达资本", "蓝海巨浪资本", "卓实基金", "嘉程资本", "马笛儿投资", "晟道投资", "中关村创业大街双创基金", "兰君创投", "百度风投", "二零创投", "星创投", "绿洲资本", "国美资本", "伯仲资本", " 金光紫金股权投资基金", "普雷资本", "小咖资本", "高鹄资本", "朗然资本", "澜亭资本", "知行资本", "云晖资本", "多维海拓", "庆芮资本", "三千资本", "英华资本", "知投资本", "云禧资本", "嘉铭浩春", "Withinlink碚曦投资", "京东金融千树资本", "国泰瑞丰", "福泉投资", "新媒创投", "零度资本", "启承资本", "厚德创投孵化器", "易翎资本", "优领资本", "银领资本", "硬币资本INBlockchain", "深北创投", "古莲资本", "顶商投资", "益通资产", "蓝图创投", "星合资本", "华峰资本", "不惑创投", "盛港投资", "高娱资本", "如码资本", "新番资本", "乾德资本", "冲盈资本", "凌晨资本", "聚众资本", "五方资本", "永禧资产", "欧菲和正投资", "谷米移基金", "几何投资(中国教育投资基金)", "厚达资本", "酉金资本Regent Capital", "明峰资本", "深南创投", "鼎域恒睿", "北纬资本", "九宜城", "杰克利奥资本JACKLEO Capital", "真成投资", "一臂资本ArmVC", "沐芃闪投", "中盈美盛", "海煦资本", "天安金控", "21基金", "元生创投", "中视资本", "泛舟资本", "中美绿色基金", "敦鸿资产", "时龙资本", "安兰资本(华隆集团)", "众合瑞民", "红山基金", "势能资本", "先锋国盛", "丰盛资本", "东方盛鼎", "申圳投资", "前海恒昇基金", "馨企投资(银禾资本)", "沣扬资本", "合创资本", "和高资本(和凯创投)", "岩海投资", "晟初投资", "龙珠资本(美团点评产业基金)", "鸿泰基金", "千程投资", "Auto Space车创", "中域资本", "中海资本", "歌斐教育", "纳德资本", "险峰旗云", "大一资本", "光量资本", "宏奇资本", "儒艺资本", "高鹏资本", "相兑投资EWI Investments", "节点资本", "东方新创", "海贝资本", "奇势资本", "宏时资本", "三羊基金", "星链资本", "LinkVC连接资本", "清科辰光教育基金", "华青资本", "Bits x Bites", "东部资本(东部众创)", "景裕资产", "拼图资本", "千方基金ChainFunder", "科银资本Collinstar Capital", "星辰资本", "维京资本", "时戳资本", "JLAB投资", "丁香汇创投", "景旭创投", "华美基金", "瀚丰资本", "梁山资本", "国鹏资本", "氢创投资", "协同投资", "中金智德", "杭州水木基金", "融通高科创投", "中金资本", "区块链产业基金", "科零创投", "UFO创投", "文承资本", "DFund", "FBG Capital", "8VC", "BlockVC", "润石资本", "华资资本", "贞一众创空间", "子竹资产", "华医资本", "壹诺创投", "启诚资本", "之宝创投", "映趣资本", "了得资本", "星耀资本", "BitAngel比特天使基金", "彤欣资本", "挑战者资本", "海创汇", "容铭资本", "新川资本", "弈秋资本", "联合创投", "场景实验室", "光谷人才基金", "奇点纪元", "麓谷高新创投", "中大融港创投", "千赐资本", "永创伟业", "领复资本", "达安创谷", "苏民投", "蓝烯资本", "北京奕铭投资", "隆门投资", "开物天使基金(开物相泰)", "大兵小匠", "温青创投", "歌者资本", "创想天使", "浙大联创投资", "华联长山兴", "元迅投资", "创伴投资", "弘卓资本", "泰然天合", "恩美投资", "启迪种子", "光璞资本", "溪林投资", "华图资本", "东方翌睿", "国投创业", "君和永道", "国投创合", "反身资本", "国信国投", "国投科创", "ZPF中关村并购母基金", "星燎资本", "臻值资本", "青岳资本", "沂景投资", "东资基金", "中云辉资本", "中青旅红奇基金", "七熹投资", "夸克创投", "夸克资本", "蔚来资本", "丝路华创", "高朋资本", "Astar Fund", "长策投资", "宸极投资", "泽山资本", "鸥翎投资", "阿特列斯资本", "上古资本", "海子资产", "朴素资本", "交享越", "小即是大资本", "国新科创基金（国新基金）", "岩木草投资", "巨杉资产", "强云资本", "优化资本", "荒合资本", "穆达创投", "原色咨询", "长成投资(百度)", "S. Capital一致资本", "镜湖资本", "中寰资本", "Plutus区块链基金", "凡麦资本", "云懿投资", "基岩资本", "睿鼎资本", "瑞健资本", "哈希资本Hash Capital", "金沙江资本", "2049投资集团", "创璟资本", "中顺易资本", "合源资本", "晨稷投资", "信创资本", "诺思华资本", "复星瑞哲", "正念资本", "和壹资本", "安妙资本", "赤子基金", "青檬资本", "世纪华人", "博行资本", "安可资本", "广觉资本", "光济资本", "Venturous", "雄岸基金", "NutsCapital区块链基金", "八维资本", "浅月资本", "海阔天空创投", "乐东资本", "财通资本", "WestBridge Capital", "沿海资本", "邦盛资本", "斐君资本", "蓝海资本BOCG", "蓝海众力资本", "弘励创投", "比邻星创投", "昊翔资本", "新声资本", "朗科投资", "尚之诺投资", "Cormorant Asset Management", "仁智资本", "中交资产", "天玑创投", "万世资本", "银盈资本", "骁锐资本", "国仟创投", "创梦创投", "新瞳资本", "国民创投", "聚元资本", "JRR Crypto", "新湃资本", "普为资本", "紫峰资本", "御势资本", "国衡投资", "浪潮资本", "C Ventures Fund", "启创资本QC Capital", "杏泽资本", "罗煜资本", "深圳独角兽资本", "蓝枫资本", "元明资本", "水木创融", "柒壹资本", "清泉石资本", "置柏投资", "唐竹资本", "引力资本", "信义资本", "指航基金", "追梦者基金", "亦合资本", "鼎心资本", "厚合资本", "明心资本", "本体全球资本（OGC）", "J One Capital", "链上资本(链上FOF)", "有余金服", "海松资本", "蓝焱资本", "德龙资本", "共识实验室（火星生态基金）", "大钲资本", "唯君资产", "德弘资本", "源和资本", "国诚基金", "星仪资本集团", "优选资本", "普丰基金", "华创深大投资", "23Seed思得投资", "想象力基金", "开牛投资", "裂变资本", "公信资本", "比升资本", "同德资本", "巴特恩资本", "华新投资", "粤民投", "B Capital Group", "棕榈资本", "富海资本", "磐石基金", "小白资本", "GBIC", "符号资本", "Blockchain Ventures", "凯捷资本", "铠启资本", "NGC", "三峡鑫泰", "广济创投", "磁力资本", "云石资本", "清源资本Tsingyuan Ventures", "睿盟希资本", "WF Capital", "星湖资本", "则金基金", "国投智能", "星鸾资本", "同炬资本", "复昇投资", "再石资本", "元泉资本", "道合科技投资", "格局投资", "鼎和硕投资", "十维资本", "倍数资本", "想象资本", "识贝资本", "三链资本", "银杏资本", "九天创合资本", "Bitblock Capital", "粤嘉基金", "锦云投资", "银虎资本", "数字启蒙资本", "平安资本", "民族资本", "动平衡资本", "盈睿资本", "贵景资本", "火币全球生态基金", "凯融资本", "博流资本", "鸿臻投资", "富浩基金", "JMCR家族办公室", "XBOTPARK基金", "真奇资本", "一苇资本", "M31资本", "厘米空间孵化器", "百咖创投", "中联投", "Polychain Capital", "星界资本", "Airbus Ventures", "旭珩资本", "方皋创投", "菁英汇投资", "安元基金", "热点资本", "中国天禄投资", "华璋资本", "集睿资本", "有汉投资", "Spider Capital", "新宜资本", "卓悦资本", "震业集团", "同程众创启程金禾基金", "助力资本", "中瑞润和", "令牌资本", "论道投资", "智慧工场创投", "上合资本", "君灏资本", "洽雨资本", "原力创投", "东方世旗", "金石资本", "天润投行", "信修投资", "中冀投资", " 中元九派基金", "ATM capital亚洲科技媒体基金", "滢盛资本", "唯贤资本", "华宏资产", "銘丰资本", "安朴资本", "腾达资本", "度量衡资本", "清新资本", "昆吾产业", "银豹投资", "海润国际并购基金", "中硕资本", "钜鑫资本", "翔御资本", "尚腾资本", "千毅资本", "中投国资", "诚美创投", "盛沃投资", "帕拉丁资产管理", "山汇资本", "Dentsu Ventures", "高成资本", "驰星创投", "纬度创投", "久友资本", "华海投资", "本初资本", "中扶众望", "芯云资本（SilliconX.AI）", "沃生投资", "薄荷天使基金", "翼朴资本", "允治资本", "元真价值投资", "壹步资本", "EQT Ventures", "北航投资", "征和惠通", "中嵘投", "兼固资本", "丹麓资本", "新松投资", "雷达资本", "中平资本", " 华本创投", "合平资产", "诚硕资本", "万图投资", "华迎资本", "新宸盛元", "睿鲸资本", "遵理资本", "海创会资本", "链豆资本", "澄志创投", "山景资本", "中安创投", "中泽资本", "lakecapital泽悦资本", "自觉资本", "多鲸资本", "光毅资本", "京立资本", "翰鼎投资", "中信文化资本", "KoinVentures（KV资本）", "奇迹资本", "新势能基金", "聚卓资本", "禧筠资本", "慧科资本", "凌波资本", "北塔资本", "鹏万投资", "融创资本", "DNA FUND", "君桐资本", "Accomplice", "Goodwater Capital", "FJ Labs", "Digital Currency Group", "Reach Capital", "Beenext", "Venture Highway", "Tusk Ventures", "Sistema Asia Fund", "RB Investments", "Mosaic Ventures", "开弦资本", "繸子资产", "MDI Ventures", "Liquid 2 Ventures", "M12", "泽贤投资", "Felix Capital", "Sistema Venture Capital", "Axilor Ventures", "Section 32", "GreatPoint Ventures", "Fifth Wall", "Entrée Capital", "Trifecta Capital", "Fireside Ventures", "Qualgro VC", "BBG Ventures", "Presence Capital", "Zetta Venture Partners", "Precursor Ventures", "Wamda Capital", "XL Innovate", "WaterBridge Ventures", "泰亚鼎富", "Oxford Sciences Innovation", "Convergence Ventures", "Oak HC/FT", "The Venture Reality Fund", "Insignia Ventures Partners", "HIVE Ventures", "Struck Capital", "Sterling.VC", "渤溢基金", "兴橙资本", "回向基金", "和聚百川", "Endure Capital", "Eclipse Ventures", "Zeev Ventures", "千杉投资", "Daphni", "华和资本", "Wipro Ventures", "Cota Capital", "Refactor Capital", "RGAx", "Arena Ventures", "Quona Capital", "Openspace Ventures", "Alpha JWC Ventures", "OK资本", "Atami Capital", "宏商资本", "希夷资产", "Keen Venture Partners", "Inbox Capital", "High Alpha", "Arab Angel Fund", "Geodesic Capital", "极星资本", "正勤资本", "Alphabet", "正友资产", "Endiya Partners", "Afore Capital", "Abstract Ventures", "深度加速", "3One4 Capital", "Dolby Family Ventures", "Courtside Ventures", "Corazon Capital", "蛮牛投资", "Samaipata Ventures", "Unicorn India Ventures", "澜峰资本", "Rise Fund", "钱通资本", "深圳湾天使基金", "珠海科创投", "霍恩基金", "聚合资本", "Portag3 Ventures", "Orange Digital Ventures", "Omega Funds", "天狼星资本", "自贸区基金", "华盛一泓", "JAZZ Venture Partners", "Alexa Fund", "飞猪资本", "中科院创投", "陀螺创投Top Ventures", "长路体育", "连一资本", "联合基金", "谢诺辰途", "waterdrip capital水滴资本", "珂玺资本", "灏源资本", "循理资本", "英溢资本", "致云基金", "联创东林", "盈港资本", "甬潮创投", "腾讯众创空间", "猎人资本H.Capital", "盛泉资产", "SeedPlus", "广东文投创工场（广文投）", "紫竹小苗基金", "Rosecliff Ventures", "Rethink Impact", "和骞投资", "光华资本", "毅仁资本", "价值资本", "仁爱资本", "临芯投资", "中弘金控", "万朋资本", "创合汇资本"]

## Functions for producing the
def get_all_names(doc):
    lead_name = None
    rest_names = []
    for inv in doc["investor"]:
        if "invst_name" in inv.keys():
            if lead_name == None:
                lead_name = inv["invst_name"]
            else:
                rest_names += [inv["invst_name"]]
        elif "com_name" in inv.keys():
            if lead_name == None:
                lead_name = inv["com_name"]
            else:
                rest_names += [inv["com_name"]]
        else:
            pass
    return lead_name, rest_names

def convert_money(money_string):
    currency = None
    shi = "十" in money_string
    bai = "百" in money_string
    qian = "千" in money_string
    wan = "万" in money_string
    yi = "亿" in money_string

    num_part = re.findall(r"[-+]?\d*\.\d+|\d+", money_string)
    if len(num_part) == 0:
        num_part = 1
    else:
        num_part = float(num_part[0])

    amt = num_part
    if shi: amt *= 10
    if bai: amt *= 100
    if qian: amt *= 1000
    if wan: amt *= 10000
    if yi: amt *= 100000000

    if money_string[-1] == "币":
        currency = "rmb"
    elif money_string[-1] == "元":
        currency = "usd"
    else:
        currency = "other"

    return int(amt), currency

def populate_masterdict(mongo, doc):
    if doc["year"] < 2014: return
    lead_investor, follow_investors = get_all_names(doc)
    datestring = str(doc["year"]) + "-" + str(doc["month"]) + "-" + str(doc["day"])
    mongo.all_investments += \
    [
        {
        "name": doc["name"],
        "valuation": doc["valuation"] * 1000,
        "money": doc["money"],
        "date": datestring,
        "round": doc["round"],
        "com_scope": doc["com_scope"],
        "com_sub_scope": doc["com_sub_scope"],
        "investors": [lead_investor] + follow_investors,
        "syndicated": (len(follow_investors) > 0),
        "type": "not_final"
        }
    ]


    if len(doc["investor"]) > 0:
        mongo.total_investors.add(lead_investor)
        mongo.total_startups.add(doc["name"])
        mongo.total_investment_events.add(doc["id"])
        if len(follow_investors) > 0:
            mongo.networked_startups.add(doc["name"])
            safe_add(lead_investor, mongo.lead_count)
            safe_add(lead_investor, mongo.overall_count)
            mongo.networked_investors.add(lead_investor)
            mongo.networked_investors.add(lead_investor)
            mongo.networked_investment_events.add(doc["id"])
            safe_add(doc["year"],mongo.year_count)
            for fol in follow_investors:
                ### TODO: UPDATE mongo.companies, above ahve a part that updates mongo.syndicated_companies
                mongo.master_dict[
                    (lead_investor, fol, datestring)] \
                    = {
                       "name": doc["name"],
                       "money": doc["money"],
                       "valuation": doc["valuation"],
                       "round": doc["round"],
                       "com_scope": doc["com_scope"],
                       "com_sub_scope": doc["com_sub_scope"]
                       }
                safe_add(fol, mongo.follow_count)
                safe_add(fol, mongo.overall_count)
                mongo.networked_investors.add(fol)
                mongo.total_investors.add(fol)


def populate_fully_connected_masterdict(mongo, companies = False):
    docs = list(mongo.invest_event.find())
    for doc in docs:
        # if doc["year"] < 2014: return
        # if doc["year"] >= 2016: return
        lead_investor, follow_investors = get_all_names(doc)
        all_investors = [lead_investor] + follow_investors
        datestring = str(doc["year"]) + "-" + str(doc["month"]) + "-" + str(doc["day"])

        amt, currency = convert_money(doc["money"])
        valuation, round = "n/a", "n/a"
        if companies:
            if doc["name"] in mongo.companies.keys():
                valuation = mongo.companies[doc["name"]]["valuation"]
                round = mongo.companies[doc["name"]]["round"]

        mongo.all_investments += \
        [
            {
            "name": doc["name"],
            "valuation": doc["valuation"] * 1000,
            "money": amt,
            "currency": currency,
            "date": datestring,
            "round": doc["round"],
            "com_scope": doc["com_scope"],
            "com_sub_scope": doc["com_sub_scope"],
            "investors": all_investors,
            "syndicated": (len(all_investors) > 1),
            "type": "not_final",
            "final_val": valuation,
            "final_round": round
            }
        ]

        if len(doc["investor"]) > 0:
            for i in range(len(all_investors)):
                safe_add(all_investors[i], mongo.overall_count)
                for j in range(i+1,len(all_investors)):
                        mongo.master_dict[
                            (all_investors[i], all_investors[j], datestring)] \
                            = {
                               "name": doc["name"],
                               "money": amt,
                                "currency": currency,
                               "valuation": doc["valuation"],
                               "round": doc["round"],
                               "com_scope": doc["com_scope"],
                               "com_sub_scope": doc["com_sub_scope"],
                                "investors": all_investors,
                                "final_val": valuation,
                                "final_round": round
                               }
                        safe_add(all_investors[j], mongo.overall_count)


def generate_and_save_graph(mongo):
    docs = list(mongo.invest_event.find())
    for doc in docs:
        populate_masterdict(mongo, doc)

    with open("files/generate_graph.txt", "w+") as f:
        f.write(str(mongo.master_dict))
    with open("files/generate_graph.bin", "wb+") as f:
        import pickle
        pickle.dump(mongo.master_dict,f)

    for k, v in mongo.master_dict.items():
        amt, currency = convert_money(v["money"])
        mongo.master_dict[k] = {
            "name": v["name"],
            "money": amt,
            "currency": currency,
            "valuation": v["valuation"],
            "round": v["round"],
            "com_scope": v["com_scope"],
            "com_sub_scope": v["com_sub_scope"]
        }

    with open("files/generate_graph_edited.txt", "w+") as f:
        f.write(str(mongo.master_dict))

    # print(mongo.master_dict)