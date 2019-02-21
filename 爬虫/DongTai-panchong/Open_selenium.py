from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import datetime
import codecs
class QunaSpider():
    def __init__(self):
        self.title=[]
        self.xinxi=[]
    def get_hotel(self,page_url,to_city,fromdate,todate):
        driver=webdriver.Firefox()
        driver.get(page_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"酒店").click()
        time.sleep(3)
        driver.find_element(By.NAME,'toCity').clear()#定位目的地
        driver.find_element(By.NAME,'toCity').send_keys(to_city)
        driver.find_element(By.NAME,'toCity').click()

        driver.find_element(By.ID,'fromDate').clear()#入住日期
        driver.find_element(By.ID,'fromDate').send_keys(fromdate)

        driver.find_element(By.ID,'toDate').clear()#离店日期
        driver.find_element(By.ID,'toDate').send_keys(todate)
        time.sleep(4)
        try:
            driver.find_element(By.LINK_TEXT, "搜  索").click()
        except:
            driver.find_element(By.CLASS_NAME, 'search-button js_btnsearch').click()
        finally:
            print("报错了")
        #driver.find_element(By.CLASS_NAME,'search-button js_btnsearch').click()
        page_num=0
        while True:
            try:#显示等待，判断to_city是否在当前页面
                WebDriverWait(driver,10).until(
                    EC.title_contains(to_city)
                )
            except Exception as e:
                print(e)
                break
            time.sleep(5)

            js="window.scrollTo(0,document.body.scrollHeight);"#js脚本把网页拉到底部
            driver.execute_script(js)#执行JS脚本
            time.sleep(5)

            html_content=driver.page_source#获取网页源代码

            soup=BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')#获取soup对象
            infos=soup.find_all(class_='item_hotel_name')
            # f=codecs.open(to_city+fromdate+u'.html','a','utf-8')
            #f=open('wenjian.csv','w',encoding='utf-8')
            titles=infos.find_all('a',class_='e_title js_list_name')['title']#获取酒店名称
            self.title.append(titles)#将酒店名称添加至title中
            address=infos.find_all('em').string#获取酒店地址信息
            self.title.append(address)#添加至title中
            dianping=infos.find_all('a',class_='js_list_comment_content_shanghai_city_23390 js_list_comment')['title']
            self.title.append(dianping)
            pingfen=infos.find_all('a',class_='js_list_score').b.string
            self.title.append(pingfen)
            price=infos.find_all('p',class_='item_price js_hasprice').b.string
            self.title.append(price)
            with open('wenjian.csv','w')as f:
                f_csv=csv.writer(f)
                f_csv.writerow(self.title)
                f.close()
            try:
                next_page=WebDriverWait(driver,10).until(
                    EC.visibility_of(driver.find_element(By.CLASS_NAME,'.num.icon-tag'))
                )
                next_page.click()
                page_num+=1
                time.sleep(10)
            except Exception as e:
                print(e)
                break

    def crawl(self,page_url,to_city):
        today=datetime.date.today().strftime('%Y-%m-%d')
        tomorrow=datetime.date.today()+datetime.timedelta(days=1)
        tomorrow=tomorrow.strftime('%Y-%m-%d')
        self.get_hotel(page_url,to_city,today,tomorrow)
if __name__=='__main__':
    spider=QunaSpider()
    spider.crawl('https://www.qunar.com/',u'上海')







