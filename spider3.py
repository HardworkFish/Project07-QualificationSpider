from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(
    host='localhost',  # mysql服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='******',  # 密码
    db='cehuizizhi',  # 数据库名称
    charset='utf8',  # 连接编码，根据需要填写
)

cur = conn.cursor()  # 创建并返回游标
sqla = '''
create table if not exists cehuizizhi_gd3(
        name VARCHAR(100),
        qulification_code varchar(50),
        type varchar(100),
        qulification_grade varchar(50),
        position varchar(50)
        ) DEFAULT CHARSET=utf8;

'''
a = cur.execute(sqla)
conn.commit()

browser = webdriver.Chrome()
for k in range(2, 5):
    # url = 'http://zwfw.nasg.gov.cn/search/zzdw?keyWord=&zzdj=' + str(j) + '&provice=44'
    for i in range(1, 44):
        # url = "http://zwfw.nasg.gov.cn/search/zzdw?keyWord=&pageIndex=" + str(i) + "&zzdj=1"
        url = 'http://zwfw.nasg.gov.cn/search/zzdw?keyWord=&pageIndex='+str(i) + '&zzdj=' + str(k) + '&provice=44'
        browser.get(url)
        bps = browser.page_source
        soup = BeautifulSoup(bps, 'lxml', from_encoding='utf-8')  # 隐式等待时间
        browser.implicitly_wait(3)
        result = {}
        titles = soup.find_all('span', class_='minchen')
        infos = soup.find_all('span', class_='cang')
        i = 0
        if len(titles) == 0:
            break
        for j in range(0, len(infos), 4):
            print(infos[j].get_text().strip())
            sqla = '''
                           insert into cehuizizhi_gd3(name, qulification_code,type,  qulification_grade, position)
                                           VALUES (%s,%s,%s,%s,%s);
                   '''
            cur.execute(sqla,
                        (titles[i].get_text().strip(), infos[j].get_text().strip(), infos[j + 1].get_text().strip(),
                         infos[j + 2].get_text().strip(), infos[j + 3].get_text().strip()))
            conn.commit()
            i += 1

cur.close()
conn.close()