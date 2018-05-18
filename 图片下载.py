import urllib.request
import os,sys
import time
import datetime
from bs4 import BeautifulSoup
import requests
import re  

# source url
# http://www.cartoonmad.com/comic/125600612004001.html
# from 001 to 004, 005 is not exist.

# BigUrl is the link that we can see in the webbrowse
# ur is the link that be hidden in the BigUrl

#  create a new Folder
def createFile(name):
    
    path = os.getcwd()
    #path =C:\Users\kaiyi\Documents\GitHub\MangaDownloader      

    if not os.path.exists(path+name):
        os.makedirs(path+name)
        print("New path is created");
        path = path + name
        return path;
        
    else:
        print("This path is exist!")
        return path+name;
  
# change Path    
def createPath(name):
    print("old path: "+str(os.getcwd()))
    newPath = createFile("//"+name)
    os.chdir(newPath)
    print("new path: "+str(os.getcwd()))
    print("you can do it now")
    

#3 from BigUrl get small url 
def getPhotoUrl(BigUrl):
    
    #通过request获得内容
    htmlext = requests.get(BigUrl).text
    #使用BeautifulSoup模块来解析html源码
    soup = BeautifulSoup(htmlext,'html.parser')
    images = soup.find_all('img')
    
    #先设定url为空
    url = None
    
    # 执行循环，找到合适的 图片链接
    for image in images:
        
        if 'http://web.cartoonmad.com' in image['src']:
            url = image['src']
            break
        
        if 'http://web2.cartoonmad.com' in image['src']:
            url = image['src']
            break
        
        if 'http://web3.cartoonmad.com' in image['src']:
            url = image['src']
            break
        
    # 如果url仍是为空，则无图，返回
    if url is None:
        return ;
    # 返回找到url 地址
    return url

# http://www.cartoonmad.com/comic/125600612004001.html

#4 make small url into list
def getPhotoList(BigUrl):
    
    photoList = []
    
    for i in range(1,40):
        
        if i/10 < 1.0:
            BigUrl = BigUrl[0:-6]+str(i)+".html"
        else:
            BigUrl = BigUrl[0:-7]+str(i)+".html"
            
        temp = getPhotoUrl(BigUrl)
        
        if temp == None:
            break;
        
        photoList.append(temp)
    print("The Number of photo is: "+str(len(photoList)))
    return photoList






def MangaDownloader(photoList):
    for photo in photoList:
        print("photo adress is: "+photo)
        name = photo[-7:]
        print("photo'name is :"+name)
        

        req = urllib.request.urlopen(photo)
        with open(name , 'wb') as f:
            f.write(req.read()) 
        
        print(name+ ' be downloaded!')
        print("************")
        
        
    
def getTitle(BigUrl):
    htmlext = requests.get(BigUrl)
    htmlext.encoding = 'big5'
    htmlext = htmlext.text
    #使用BeautifulSoup模块来解析html源码
    soup = BeautifulSoup(htmlext,'html.parser')
    title = soup.title.string
    return title


# =============================================================================
# BigUrl = "http://www.cartoonmad.com/comic/489700012051001.html"
# photoList = []
# photoList = getPhotoList(BigUrl)
# title = getTitle(BigUrl)
# createPath(str(title))
# MangaDownloader(photoList)
# =============================================================================
GientUrl = "http://www.cartoonmad.com/comic/5500.html"

def getBigUrlList(GientUrl):
    htmlext = requests.get(GientUrl).text
    bigUrlList = []
    soup = BeautifulSoup(htmlext,'html.parser')
    numbers = soup.find_all(name = 'a', attrs={"href":re.compile(r'\d{10,15}')})
    
    for number in numbers:
        bigUrlList.append("http://www.cartoonmad.com"+number["href"])
    return bigUrlList

path = os.getcwd()
for BigUrl in bigUrlList:
    photoList = []
    photoList = getPhotoList(BigUrl)
    title = getTitle(BigUrl)
    # reset path
    os.chdir(path)
    createPath(str(title))
    MangaDownloader(photoList)