import requests
from selenium import webdriver
from lxml import etree
import csv
import sys
# reference: http://tw.pyladies.com/~marsw/crawler02.slides.html#/3

url = sys.argv[1]

driver = webdriver.PhantomJS(executable_path='D:/PythonTest/crawler/hack/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get(url)
pageSource = driver.page_source
driver.close()

page = etree.HTML(pageSource)
try:
    tags = page.xpath('//*[@id="ProdNick"]/text()')
    tagtotal =''
    for tag in tags:
        tagtotal += tag
    print(tagtotal)
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


# file = open('product_data.csv', 'w')
# csvCursor = csv.writer(file)
# csvCursor.writerow([tagtotal, tags2, tags3])
# file.close()