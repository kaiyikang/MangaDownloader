import urllib.request
import os
import time
import datetime


os.chdir('D:\\')
os.getcwd()

# http://web4.cartoonmad.com/c86eo736r62/3583/122/050.jpg
url = 'http://web4.cartoonmad.com/c86eo736r62/3583/122/0'

def MangaDownloader(url_part):
    starttime = time.clock()
    try:
        for i in range(1,100,1):
            if i <10:
                i = str(0)+str(i)

            houzhui = str(i)+'.jpg'

            name = 'D:\\0' + houzhui

            url_full = url_part + houzhui

            req = urllib.request.urlopen(url_full)

            with open(name , 'wb') as f:
                f.write(req.read())

            print(str(i)+ ' downloaded!')
            break
    except:
        endtime = time.clock()
        print('运行时间:%d' %(endtime-starttime))
        print('异常：页数超载，结束')




MangaDownloader(url)