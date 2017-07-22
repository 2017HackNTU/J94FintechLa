import requests
from selenium import webdriver
from lxml import etree
import re
import csv
import sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# reference: http://tw.pyladies.com/~marsw/crawler02.slides.html#/3

# change to mobile website
# url = sys.argv[1]
# match = re.split(r'\?', 'http://24h.pchome.com.tw/prod/DGAD7P-A9007UFW1?q=/S/DGADAH')
# url = match[0]
# url = url[:11] + 'm.' + url[11:]

driver = webdriver.PhantomJS(executable_path=r'path_to_phantomjs/bin/phantomjs')
driver.get(url)
pageSource = driver.page_source
driver.close()

page = etree.HTML(pageSource)
try:
    tags = page.xpath('//*[@id="ProdNick"]/text()')
    tagtotal =''
    for tag in tags:
        tagtotal += tag
    print(tagtotal.strip())
except:
    print("name craw fail")
try:
    tags2 = page.xpath('//*[@id="ProdInfo"]/ul[1]/li[1]/span/span/text()')[-1]
    print(tags2)
except:
    print("price craw fail")
try:
    tags3 = page.xpath('//*[@id="ProdImg"]/img/@src')[-1]
    print(tags3)
except:
    print("img craw fail")