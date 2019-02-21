import random
import time,threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,ctime
'''
def open1(url,time): 
    driver=webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(time)
    print("open %s is ok"% url)
t1=threading.Thread(target=open1,name="thread_1",args=("www.baidu.com",10))
t2=threading.Thread(target=open1,name="thread_2",args=("www.sogou.com",10))
t1.start()
t2.start()
t1.join()
t2.join()
print("%s ended" % threading.current_thread().name)
'''
'''
def music(func,loop):
    for i in range(loop):
        print("I was listening to %s! %s" % (func,ctime()))
        sleep(2)
def movie(func,loop):
    for i in range(loop):
        print("I was at the %s %s" % (func,ctime()))
        sleep(2)
threadings=[]
t1=threading.Thread(target=music,args=('爱情买卖',2))
threadings.append(t1)
t2=threading.Thread(target=movie,args=('阿凡达',2))
threadings.append(t2)
if __name__=='__main__':
    for t in threadings:
        t.start()
    for t in threadings:
        t.join()
    print("all end %s"% ctime() )
''''''
def super_music(file_,time):
    for i in range(2):
        print("Start playing: %s %s"% (file_,ctime()))
        sleep(time)
lists={'爱情买卖.mp2':3,'阿凡达':4,'我和你':5}#参数化
threadings=[]
for file_,time in lists.items():
    t=threading.Thread(target=super_music,args=(file_,time))
    threadings.append(t)
files=range(len(lists))
if __name__=='__main__':
    for t in files:
        threadings[t].start()
    for t in files:
        threadings[t].join()
'''
def test_baidu(browser,search):
    print("start : %s" % ctime())
    print("browser : %s" % browser)
    if browser=="ff":
        driver=webdriver.Firefox()
    elif browser=="ie":
        driver=webdriver.Ie()
    elif browser=="chrome":
        driver=webdriver.Chrome()
    else:
        print("参数有误。。。。")
    driver.get("http://www.baidu.com")
    driver.find_element(By.ID,'kw').send_keys(search)
    driver.find_element(By.ID,'su').click()
    sleep(2)
    driver.quit()
lists={'chrome':'threading','ff':'python','ie':'webdriver'}
threadings=[]
for browser,search in lists.items():
    t=threading.Thread(target=test_baidu,args=(browser,search))
    threadings.append(t)
files=range(len(lists))
if __name__=='__main__':
    for t in files:
        threadings[t].start()
    for t in files:
        threadings[t].join()
