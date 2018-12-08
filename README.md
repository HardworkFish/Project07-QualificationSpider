##### Project Description(spider1.py)


1. 目标网站: [广东省测绘资质企业管理系统](http://www.cehuizizhi.com/GD/Query/1/1)

从中获取乙丙丁企业的基本信息

2. 存储格式：存入 Mysql 数据库中

##### Environment

+ Python3.6.3
+ Selenium 3.8.0
+ Chromedriver V2.41
+ Chrome 版本 67.0.3396.99
+ chromedriver 镜像地址可查看 [npm.taobao.org](http://npm.taobao.org/mirrors/chromedriver/)

##### Result

数据样例
```
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=9', 'company': '茂名市城规勘察测绘院有限公司', 'qulification_grade': '乙级', 'address': '广东省茂名市官渡南路428号', 'postcode': '525000', 'contact': '黄维腾', 'phone': '0668-3385508', 'certification': '乙测资字4410048', 'certification_issuancedate': '2017/12/14', 'deadline_time': '2019/12/31', 'bisiness': '乙级：工程测量：控制测量(三等以下。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、矿山测量(矿区控制面积200平方公里以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=26', 'company': '深圳市易行网交通科技有限公司', 'qulification_grade': '乙级', 'address': '深圳市福田区车公庙福安大厦东座7楼', 'postcode': '518040', 'contact': '邢丹丹', 'phone': '0755-26969334', 'certification': '乙测资字4410847', 'certification_issuancedate': '2018/4/19', 'deadline_time': '2019/12/31', 'bisiness': '乙级：互联网地图服务：地理位置定位、地理信息上传标注。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=27', 'company': '广东正方圆工程咨询有限公司', 'qulification_grade': '乙级', 'address': '广州市沿江中路195号沿江大厦3楼', 'postcode': '510115', 'contact': '陈丹', 'phone': '020-83362606', 'certification': '乙测资字4411416', 'certification_issuancedate': '2014/12/18', 'deadline_time': '2019/12/31', 'bisiness': '乙级：工程测量：控制测量(三等以下。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、水利工程测量(不得承担特大型水利水电工程。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、矿山测量(矿区控制面积200平方公里以下。)；海洋测绘：海域权属测绘、海岸地形测量(100平方公里以下。)、水深测量(100平方公里以下。)、水文观测(100平方公里以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=28', 'company': '广州市红鹏直升机遥感科技有限公司', 'qulification_grade': '乙级', 'address': '广州高新技术产业开发区科学城开源大道11号B7栋第六层', 'postcode': '510000', 'contact': '罗坚明', 'phone': '020-32219962', 'certification': '乙测资字4411173', 'certification_issuancedate': '2018/7/2', 'deadline_time': '2019/12/31', 'bisiness': '乙级：测绘航空摄影：一般航摄(影像地面分辨率优于0.2m，1000平方公里以下；0.2m，2000平方公里以下；0.2m~1m，30000平方公里以下。)、无人飞行器航摄(摄像地面分辨率优于0.2m，1000平方公里以下；0.2m，2000平方公里以下；0.2m~1m，30000平方公里以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=29', 'company': '江门市国土测绘大队', 'qulification_grade': '乙级', 'address': '江门市江海一路83号', 'postcode': '529000', 'contact': '李景明', 'phone': '0750-3863609', 'certification': '乙测资字4412464', 'certification_issuancedate': '2017/11/14', 'deadline_time': '2019/12/31', 'bisiness': '乙级：大地测量：卫星定位测量(Ｃ级以下。不得承担全球导航卫星系统连续运行基准站建设。)、水准测量(三等以下)、大地测量数据处理(相应于上述限额)；摄影测量与遥感：摄影测量与遥感外业、摄影测量与遥感内业；地理信息系统工程：地理信息数据采集(设区的市级行政区域以下。)、地理信息数据处理(设区的市级行政区域以下。)、地理信息系统及数据库建设(设区的市级行政区域以下。)、地理信息软件开发；工程测量：控制测量(三等以下。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、矿山测量(矿区控制面积200平方公里以下。)、工程测量监理(相应于上述限额。)；不动产测绘：地籍测绘(日常地籍调查及设区的市级以下地籍总调查中的地籍测绘。)、房产测绘(规划许可证载单栋建筑面积10万平方米以下；单个合同标的不超过建筑面积200万平方米。)、行政区域界线测绘、不动产测绘监理(相应于上述限额。)；地图编制：地形图(省级及以下行政区域范围内。)、全国及地方政区地图(省级及以下行政区域范围内。)、电子地图(省级及以下行政区域范围内。)、真三维地图(省级及以下行政区域范围内。)、其他专用地图(省级及以下行政区域范围内。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=2', 'company': '深圳市房行天下网络科技有限公司', 'qulification_grade': '乙级', 'address': '深圳市南山区深南大道9789号德赛科技大厦20层2001A室(楼宇标识为2204室）', 'postcode': '518000', 'contact': '陈健群', 'phone': '0755-83760616', 'certification': '乙测资字4410829', 'certification_issuancedate': '2014/11/28', 'deadline_time': '2019/12/31', 'bisiness': '乙级：互联网地图服务：地理位置定位、地理信息上传标注。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=31', 'company': '广州市房地产信息中心', 'qulification_grade': '乙级', 'address': '广州市豪贤路193号3楼', 'postcode': '510030', 'contact': '赵昕', 'phone': '020-83194002', 'certification': '乙测资字4411440', 'certification_issuancedate': '2014/12/18', 'deadline_time': '2019/12/31', 'bisiness': '乙级：互联网地图服务：地理位置定位、地理信息上传标注。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=35', 'company': '广州博纳信息技术有限公司', 'qulification_grade': '乙级', 'address': '广州市越秀区东风东路745号1802、1803房', 'postcode': '510080', 'contact': '林嘉仪', 'phone': '020-83642845', 'certification': '乙测资字4411047', 'certification_issuancedate': '2017/5/15', 'deadline_time': '2019/12/31', 'bisiness': '乙级：地理信息系统工程：地理信息数据采集(设区的市级行政区域以下。)、地理信息数据处理(设区的市级行政区域以下。)、地理信息系统及数据库建设(设区的市级行政区域以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=40', 'company': '深圳市深水水务咨询有限公司', 'qulification_grade': '乙级', 'address': '深圳市罗湖区黄贝街道延芳路63号', 'postcode': '518003', 'contact': '宋纯', 'phone': '0755-22385963', 'certification': '乙测资字4411137', 'certification_issuancedate': '2017/7/7', 'deadline_time': '2019/12/31', 'bisiness': '乙级：摄影测量与遥感：摄影测量与遥感外业；地理信息系统工程：地理信息数据采集(设区的市级行政区域以下。)；工程测量：控制测量(三等以下。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、变形形变与精密测量(一般精密设备安装。建筑面积在10万平方米以下且高度在100m以下的建筑。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、水利工程测量(不得承担特大型水利水电工程。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、地下管线测量(管线长度300km以下。)、矿山测量(矿区控制面积200平方公里以下。)；不动产测绘：地籍测绘(日常地籍调查及设区的市级以下地籍总调查中的地籍测绘。)、房产测绘(规划许可证载单栋建筑面积10万平方米以下；单个合同标的不超过建筑面积200万平方米。)；大地测量：卫星定位测量(Ｃ级以下。不得承担全球导航卫星系统连续运行基准站建设。)、水准测量(三等以下)、三角测量(三等以下)、大地测量数据处理(相应于上述限额)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=63', 'company': '广东科诺勘测工程有限公司', 'qulification_grade': '乙级', 'address': '广东省广州市萝岗区天丰路1号办公区内自编三栋二楼全层、三楼全层', 'postcode': '510663', 'contact': '曹晶', 'phone': '020-32116184', 'certification': '乙测资字4411459', 'certification_issuancedate': '2017/6/5', 'deadline_time': '2019/12/31', 'bisiness': '乙级：大地测量：卫星定位测量(Ｃ级以下。不得承担全球导航卫星系统连续运行基准站建设。)、水准测量(三等以下)、三角测量(三等以下)、大地测量数据处理(相应于上述限额)；测绘航空摄影：无人飞行器航摄(影像地面分辨率优于0.2m，50平方公里以下；0.2m，400平方公里以下；0.2m~1m，500平方公里以下。)；摄影测量与遥感：摄影测量与遥感外业、摄影测量与遥感内业；地理信息系统工程：地理信息数据采集(设区的市级行政区域以下。)、地理信息数据处理(设区的市级行政区域以下。)、地理信息软件开发、地理信息系统及数据库建设(设区的市级行政区域以下。)；工程测量：矿山测量(矿区控制面积200平方公里以下。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、控制测量(三等以下。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、变形形变与精密测量(一般精密设备安装。建筑面积在10万平方米以下且高度在100m以下的建筑。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、水利工程测量(不得承担特大型水利水电工程。)、地下管线测量(管线长度300km以下。)；海洋测绘：海域权属测绘、海岸地形测量(100平方公里以下。)、扫海测量(100平方公里以下。)、水深测量(100平方公里以下。)、水文观测(100平方公里以下。)、海洋工程测量(100平方公里以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=68', 'company': '中铁广州工程局集团有限公司', 'qulification_grade': '乙级', 'address': '广州市花都区建设路34号', 'postcode': '510800', 'contact': '张健其', 'phone': '020-89680871', 'certification': '乙测资字4411369', 'certification_issuancedate': '2018/4/19', 'deadline_time': '2019/12/31', 'bisiness': '乙级：工程测量：地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、变形形变与精密测量(一般精密设备安装。建筑面积在10万平方米以下且高度在100m以下的建筑。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、控制测量(三等以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=76', 'company': '广州运维电力科技有限公司', 'qulification_grade': '乙级', 'address': '广州高新技术产业开发区科学城彩频路7号之一801、803房', 'postcode': '510663', 'contact': '雍琪', 'phone': '020-82115706', 'certification': '乙测资字4412338', 'certification_issuancedate': '2017/3/3', 'deadline_time': '2019/12/31', 'bisiness': '乙级：地理信息系统工程：地理信息数据采集(设区的市级行政区域以下。)、地理信息数据处理(设区的市级行政区域以下。)、地理信息系统及数据库建设(设区的市级行政区域以下。)、地理信息软件开发；工程测量：控制测量(三等以下。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、地下管线测量(管线长度300km以下。)；地图编制：电子地图(省级及以下行政区域范围内。)、真三维地图(省级及以下行政区域范围内。)、其他专用地图(省级及以下行政区域范围内。)；不动产测绘：地籍测绘(日常地籍调查及设区的市级以下地籍总调查中的地籍测绘。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=79', 'company': '江门市城市地理信息中心', 'qulification_grade': '乙级', 'address': '江门市堤东路129号', 'postcode': '529000', 'contact': '韦景尧', 'phone': '0750-3160692', 'certification': '乙测资字4412151', 'certification_issuancedate': '2018/3/29', 'deadline_time': '2019/12/31', 'bisiness': '乙级：地理信息系统工程：地理信息数据处理(设区的市级行政区域以下。)、地理信息系统及数据库建设(设区的市级行政区域以下。)、地理信息软件开发、地理信息系统工程监理(相应于上述限额。)；地图编制：地形图(省级及以下行政区域范围内。)、全国及地方政区地图(省级及以下行政区域范围内。)、电子地图(省级及以下行政区域范围内。)、真三维地图(省级及以下行政区域范围内。)、其他专用地图(省级及以下行政区域范围内。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=73', 'company': '广东泊锐数创空间技术有限公司', 'qulification_grade': '乙级', 'address': '惠州市仲恺高新区惠风东二路16号B栋203 ', 'postcode': '516006', 'contact': '李金峁', 'phone': '0752-3290444', 'certification': '乙测资字4410739', 'certification_issuancedate': '2017/4/24', 'deadline_time': '2019/12/31', 'bisiness': '乙级：测绘航空摄影：一般航摄(影像地面分辨率优于0.2m，1000平方公里以下；0.2m，2000平方公里以下；0.2m~1m，30000平方公里以下。)、无人飞行器航摄(摄像地面分辨率优于0.2m，1000平方公里以下；0.2m，2000平方公里以下；0.2m~1m，30000平方公里以下。)；摄影测量与遥感：摄影测量与遥感外业、摄影测量与遥感监理、摄影测量与遥感内业；地理信息系统工程：地理信息数据采集(设区的市级行政区域以下。)、地理信息数据处理(设区的市级行政区域以下。)、地理信息系统及数据库建设(设区的市级行政区域以下。)、地理信息软件开发、地理信息系统工程监理(相应于上述限额。)；工程测量：控制测量(三等以下。)、地形测量(1：500比例尺，30平方公里以下；1：1000比例尺，50平方公里以下；1：2000比例尺，80平方公里以下；1：5000比例尺，100平方公里以下；1：1万比例尺，200平方公里以下。)、规划测量(总建筑面积50万平方米以下；国家重点建设工程不得承担。)、建筑工程测量(建筑范围1平方公里以下，单个建筑物10万平方米以下。)、市政工程测量(特大城市一般道路、大中等城市主干道路、一般立交桥。)、线路与桥隧测量(300km以下的线路，多孔跨径总长在100m以下的桥梁，4km以下的隧道。)、矿山测量(矿区控制面积200平方公里以下。)、工程测量监理(相应于上述限额。)、水利工程测量(不得承担特大型水利水电工程。)、地下管线测量(管线长度300km以下。)、变形形变与精密测量(一般精密设备安装。建筑面积在10万平方米以下且高度在100m以下的建筑。)；不动产测绘：地籍测绘(日常地籍调查及设区的市级以下地籍总调查中的地籍测绘。)、房产测绘(规划许可证载单栋建筑面积10万平方米以下；单个合同标的不超过建筑面积200万平方米。)、行政区域界线测绘、不动产测绘监理(相应于上述限额。)；地图编制：地形图(省级及以下行政区域范围内。)、教学地图(省级及以下行政区域范围内。)、全国及地方政区地图(省级及以下行政区域范围内。)、电子地图(省级及以下行政区域范围内。)、真三维地图(省级及以下行政区域范围内。)、其他专用地图(省级及以下行政区域范围内。)；海洋测绘：海域权属测绘、海岸地形测量(100平方公里以下。)、水深测量(100平方公里以下。)、海洋测绘监理(相应于上述限额。)、水文观测(100平方公里以下。)。***'}
{'url': 'http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=85', 'company': '深圳市活力天汇科技股份有限公司', 'qulification_grade': '乙级', 'address': '深圳市南山区粤海街道高新南九道10号深圳湾科技生态园10栋B座13层01-08号', 'postcode': '518057', 'contact': '陈水燕', 'phone': '0755-86022762', 'certification': '乙测资字4410856', 'certification_issuancedate': '2018/5/28', 'deadline_time': '2019/12/31', 'bisiness': '乙级：互联网地图服务：地理位置定位、地理信息上传标注。***'}

````

