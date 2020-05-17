# # -*- coding:UTF-8 -*-
import requests
from lxml import etree
import time

head = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'pgv_pvi=8916551680; RK=TBippBisYd; ptcz=19babe465852b42945a588465bf3e52ce6f389535b2bb81227c31f5fd137312e; pgv_pvid=8738266725; _ga=amp-DfmU9VZHt6IWi4wyhjOGLw; o_cookie=648049522; pac_uid=1_648049522; ts_uid=373963030; ied_qq=o0648049522; pgv_info=ssid=s1242074467; ts_last=news.qq.com/; ts_refer=www.baidu.com/link; ad_play_index=14',
'referer': 'https://news.qq.com/zt2020/page/feiyan.htm',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0  Mobile/15A372 Safari/604.1'
}

def run(num):
    try:
        url = "http://m.tiandaoedu.com/index.php/School/school_delay_load/?count=" + str(num) + "&stage=ss&country=all&rank=all&major=all"

        data = requests.get(url, headers=head, timeout=3)
        res = data.text
        html = etree.HTML(res)
        list = html.xpath('//dl/a/@href')
        for i in list:
            print(i)
    except IOError:
        print(num)
if __name__ == '__main__':
    i = 0
    while i <= 40:
        num = i * 10
        run(num)
        i += 1
        time.sleep(10)  # 休眠1秒