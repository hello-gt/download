# -*- coding=utf8 -*-
from conf.settings import *
import time
from lxml import etree
import requests
from bs4 import BeautifulSoup
import sys
import urllib2
import demjson

head = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "ASPSESSIONIDQSSDRCTD=FBIEDBDBEAEHCBCPAHFBIMCE; safedog-flow-item=; Hm_lvt_111265fb79fb64555a529b9f0a62f7ea=1589814879; Hm_lpvt_111265fb79fb64555a529b9f0a62f7ea=1589814879",
"Host": "www.sdsgwy.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
}

def detail_url(url):
    data = requests.get(url, headers=head, timeout=3)
    res = data.text
    html = etree.HTML(res)
    list = html.xpath('.//div[@id="main-content"]/div[@class="primary"]/h2')
    print(list)

def detail(url):
    # 获取字符串格式的html_doc。由于content为bytes类型，故需要decode()
    html_doc = urllib2.urlopen(url)
    # 使用BeautifulSoup模块对页面文件进行解析
    soup = BeautifulSoup(html_doc, 'lxml')
    timu = timu_detail(soup) #题目
    print(timu)
    xuanxiang = soup.find_all("input")

    jsonData = []
    i = 0;
    for input in xuanxiang:
        jsonData.append(input)
    text = jsonData #答案和选项
    print(text)

"""
题目
"""
def timu_detail(soup):
    links = soup.h2
    images = links.find('img')
    if images is None:
        timu = links.string  # 题目
    else:
        timu = images['src']  # 题目
    return timu

if __name__ == '__main__':
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
    for item in INDEX_LIST:
        time.sleep(1)
        url = item['url']
        detail(url)