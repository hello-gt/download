# -*- coding=utf8 -*-
import urllib2
import os
from conf.settings import *
import time
import random

def getHtml(url):
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open(file_name, "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(file_content)

#详情文件名
def info_name(url):
    end_pos = url.rfind('/') - 1  # 倒数第一个"/"的位置再左移一位
    start_pos = url.rfind('/', 0, end_pos)  # 网址从开始截至到end_pos的位置，从右往左出现的第一个"/"也就是我们要找的倒数第二个"/"
    filename = url[start_pos + 1:-1]  # 截取网址的倒数第二个 "/" 后面的内容
    return filename

#列表文件名
def list_name(url):
    end_pos = url.rfind('/') - 1  # 倒数第一个"/"的位置再左移一位
    start_pos = url.rfind('/', 0, end_pos)  # 网址从开始截至到end_pos的位置，从右往左出现的第一个"/"也就是我们要找的倒数第二个"/"
    filename = url[start_pos + 1:]  # 截取网址的倒数第二个 "/" 后面的内容
    return filename

#建立目录
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + ' 目录已存在'
        return False

if __name__ == '__main__':
    for item in INDEX_LIST:
        num = random.randint(80,3000)
        time.sleep(num)
        url = item['url']
        print url + " --> "
        try:
            filename = ''
            if url.find('.html') == -1:
                #filename = 'index.html'
                #filename = info_name(url) # 院校详情文件名
                filename = list_name(url)  # 院校列表文件名
            else:
                filename = os.path.split(url)[1]
            path = HTML_DIR
            html = getHtml(url)
            print path + filename + ' saving'
            newdir = os.path.join(path,filename)
            #mkdir(newdir)
            saveHtml(newdir, html)
        except:
            print("Exception:" + url)

    print("下载成功")