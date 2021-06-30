import os
import re
import time
import datetime
import requests
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

#论文链接
thsis_url="https://thesis.lib.pku.edu.cn/docinfo.action?id1=56b030af6d7a0e566009fa151cc9a83d&id2=KhhPjCdEGOQ%253D"
driver.get(thsis_url)
driver.refresh()
time.sleep(2)
lookbut = driver.find_element_by_link_text('查看全文')
lookbut.click()
handles = driver.window_handles
driver.switch_to_window(handles[1])
time.sleep(2)
#获取总页数
tpage=driver.find_element_by_css_selector('span#totalPages.toolbar-page-num')
total_pages=int(re.sub("\D","",tpage.get_attribute("innerText")))
print('本论文总页数为：%d 页'%(total_pages))
total_pages=int(total_pages)
#下载论文
os.makedirs('./thsis_image/', exist_ok=True)
i=0
find_page=False
while i<total_pages:
    div_name='div#loadingBg%d.loadingbg > img'%(i)
    try:
        pics = driver.find_element_by_css_selector(div_name)
        find_page=True
        img_url=pics.get_attribute('src')
    except:
        find_page=False
    if find_page:
        print('找到第%d页...'%(i+1))
        #print(img_url)
        i=i+1
        urlretrieve(img_url, './thsis_image/img%d.jpg'%(i))
    else:
        btnext=driver.find_element_by_css_selector('a#btnnext.toobar-btn.toobar-btn-next')
        btnext.click()
        time.sleep(0.5)
print('文章下载完成！')