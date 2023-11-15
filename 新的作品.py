# 该程序原本实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷，现对CSDN已失效。
# 当时经过测试发现大概间隔70秒访问一下，访问量才会增加1，现对CSDN已失效。
# 只需要修改或添加url的链接就可以了(测试用的原作者CSDN文章链接)
import requests
import time
url = ['http://ywjgame.ueuo.com/Venom%20escape.html',
       'http://ywjgame.ueuo.com/3D%20shooting%20Chinese.html',
        'http://ywjgame.ueuo.com/Tower%20defense%20situation.html',
        'http://ywjgame.ueuo.com/Gunfight%20V.1.12.1.5%20Official%20release.html',
        'http://ywjgame.ueuo.com/',
        'http://ywjgame.ueuo.com/3D%20Eating%20chicken.html',
        'http://ywjgame.ueuo.com/Space%20werewolf%20killing%20-%20Chinese%20online%20version.html',
        'http://ywjgame.ueuo.com/mc%20Chinese%20version.html']
# 浏览器User-Agent
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5959.400 SLBrowser/10.0.3544.400'}   
count = 0
countUrl = len(url)
# 访问次数设置
for i in range(1,100000):
    if count < 1000000:
        try:  # 正常运行
            for i in range(countUrl):
                response = requests.get(url[i], headers=headers)
                if response.status_code == 200:
                    count = count + 1
                    print('Success ' + str(count), 'times')    
            time.sleep(0.1) # 访问间隔时间秒
        except Exception:  # 异常
            print('Failed and Retry')
            time.sleep(60) # 异常重启时间秒