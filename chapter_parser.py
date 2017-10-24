from bs4 import BeautifulSoup
import re
import urllib.parse
import requests


class MDParser(object):
    def get_all_chapter(self,download_url):
        page = []
        new_urls = []
        content = requests.get(download_url).content
        soup = BeautifulSoup(content,"html.parser",from_encoding='utf-8')
        # \/comic\/\d{15}.html
        links = soup.find_all('a', href=re.compile(r'\/comic\/\d{15}.html'))

        for link in links:
            new_url = link['href']

            new_full_url = urllib.parse.urljoin(download_url, new_url)
            new_urls.append(new_full_url)

        return new_urls
