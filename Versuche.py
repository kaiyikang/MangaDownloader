# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:50:07 2018

@author: kaiyi
"""
import urllib.request
import os,sys
import time
import datetime
from bs4 import BeautifulSoup
import requests
import re



class mangaDownloader:

    def __init__(self,gient_url):
        self.gient_url = gient_url


    def getBigUrlList(self):
        htmlext = requests.get(self.gient_url).text
        bigUrlList = []
        soup = BeautifulSoup(htmlext, 'html.parser')
        numbers = soup.find_all(name='a', attrs={"href": re.compile(r'\d{10,15}')})

        for number in numbers:
            bigUrlList.append("http://www.cartoonmad.com" + number["href"])
        return bigUrlList


    def getTitle(self,BigUrl):
        htmlext = requests.get(BigUrl)
        htmlext.encoding = 'big5'
        htmlext = htmlext.text
        # 使用BeautifulSoup模块来解析html源码
        soup = BeautifulSoup(htmlext, 'html.parser')
        title = soup.title.string
        return title

    def getPhotoUrl(self,bigUrl):
        # 通过request获得内容
        htmlext = requests.get(bigUrl).text
        # 使用BeautifulSoup模块来解析html源码
        soup = BeautifulSoup(htmlext, 'html.parser')
        images = soup.find_all('img')

        # 先设定url为空
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
            return;
        # 返回找到url 地址
        return url



    def getPhotoList(self,bigUrl):
        # 建立空的list
        photoList = []

        for i in range(1, 4):

            if i / 10 < 1.0:
                bigUrl = bigUrl[0:-6] + str(i) + ".html"
            else:
                bigUrl = bigUrl[0:-7] + str(i) + ".html"

            temp = self.getPhotoUrl(bigUrl)

            if temp == None:
                break;

            photoList.append(temp)
        print("The Number of photo is: " + str(len(photoList)))
        return photoList

    def createFile(self,name):

        path = os.getcwd()
        # path =C:\Users\kaiyi\Documents\GitHub\MangaDownloader

        if not os.path.exists(path + name):
            os.makedirs(path + name)
            print("New path is created");
            path = path + name
            return path;

        else:
            print("This path is exist!")
            return path + name;

    # change Path
    def createPath(self,name):
        print("old path: " + str(os.getcwd()))
        newPath = self.createFile("//" + name)
        os.chdir(newPath)
        print("new path: " + str(os.getcwd()))
        print("you can do it now")

    def Downloader(self,photoList):

        for photo in photoList:
            print("photo adress is: " + photo)
            name = photo[-7:]
            print("photo'name is :" + name)

            req = urllib.request.urlopen(photo)
            with open(name, 'wb') as f:
                f.write(req.read())

            print(name + ' be downloaded!')
            print("--------------------------")


    def start(self):
        print("This programm has started")
        # 设定初始化path
        path = os.getcwd()
        # 获得bigUrlList
        bigUrlList = self.getBigUrlList();
        # 对于每一个BigUrl list
        for bigUrl in bigUrlList:
            # 获得图片的列表
            photoList = self.getPhotoList(bigUrl)
            # 获得该章节的title
            title = self.getTitle(bigUrl)
            # reset path
            os.chdir(path)
            # 更改path，并建立新文件夹
            self.createPath(str(title))
            # 下载图片
            self.Downloader(photoList)










