"""
Author: TRsky
Time: 2018-12-07 22:16
Content: crawl data from cihuizizhi website
"""

import re
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
create table if not exists cehuizizhi_gd1(
        url VARCHAR(100),
        company VARCHAR(100),
        qulification_grade varchar(50),
        address varchar(120),
        postcode varchar(20),
        contact varchar(20),
        phone varchar(20) ,
        certification varchar(100) ,
        certification_issuancedate varchar(50),
        deadline_time varchar(50) ,
        bisiness text) DEFAULT CHARSET=utf8;

'''

a = cur.execute(sqla)
conn.commit()

browser = webdriver.Chrome()
browser.get('http://gdchzz.nasg.gov.cn/Index/QueryList.aspx')
# 隐式等待时间
browser.implicitly_wait(3)

# 省选择框
select_province = Select(browser.find_element_by_name('sltProvince'))
search = browser.find_element_by_id('Unit')
search.click()

# 点击搜索按钮
search_report = browser.find_element_by_id('BtnSearch')

# 匹配 id
ID_RE = re.compile(r'onclick="ShowInfo\((\d+),2\)"')
TD_RE = re.compile(r'<td class="tdleft">(.*?)</td>')

# ['企业名称', '资质等级', 'address', 'postcode', '联系人', '联系电话', '资质证号', '发证日期', '证书有效期', '单位业务范围']
pros_df = ['url', 'company', 'qulification_grade', 'address', 'postcode', 'contact', 'phone', 'certification',
           'certification_issuancedate',  'deadline_time', 'bisiness']

for province_index in range(1, len(select_province.options)):
    select_province.select_by_index(province_index)
    search_report.click()
    time.sleep(1)

    # 58
    for page in range(1, 58):
        ss = '__doPostBack("PageTurnControl1$ANPager", "%d")' % page
        browser.execute_script(ss)
        time.sleep(2)
        ids = ID_RE.findall(browser.page_source)
        for id in ids:
            url = "http://gdchzz.nasg.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?&ID=" + str(id)
            browser.get(url)
            bps = browser.page_source
            soup = BeautifulSoup(bps, 'lxml', from_encoding='utf-8')
            title = soup.find('span', id='lllName')
            items = soup.find_all('td', class_='tdright')
            result = dict()
            result[pros_df[0]] = url
            result[pros_df[1]] = title.get_text()
            result[pros_df[2]] = items[0].get_text().strip()
            result[pros_df[3]] = soup.find('span', id="lblOfficeAddress").get_text()
            result[pros_df[4]] = items[2].get_text().strip()
            result[pros_df[5]] = items[3].get_text().strip()
            result[pros_df[6]] = items[4].get_text().strip()
            result[pros_df[7]] = items[5].get_text().strip()
            result[pros_df[8]] = items[6].get_text().strip()
            result[pros_df[9]] = items[7].get_text().strip()
            result[pros_df[10]] = items[8].get_text().strip("***\n")
            print(result)
            sqla = '''
                insert into cehuizizhi_gd1(url, company, qulification_grade, address, postcode, contact,
                                phone, certification, certification_issuancedate,  deadline_time, bisiness)
                                VALUES (%s,%s,%s,%s,%s, %s,  %s,%s, %s, %s, %s);
            '''
            b = cur.execute(sqla, (result[pros_df[0]], result[pros_df[1]], result[pros_df[2]], result[pros_df[3]],
                                   result[pros_df[4]], result[pros_df[5]], result[pros_df[6]], result[pros_df[7]],
                                   result[pros_df[8]], result[pros_df[9]], result[pros_df[10]]))
            conn.commit()
        browser.get('http://gdchzz.nasg.gov.cn/Index/QueryList.aspx')
    time.sleep(1)

cur.close()
conn.close()

