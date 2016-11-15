"first set of tools: tools need by a worker to parse data"

from bs4 import BeautifulSoup
import os
from pattern import*
import time
from urllib import urlopen

#adress_finder(object)
class LinkFinder:

    def __init__(self, html, base_url):
        self.html = html
        self.base_url = base_url
        self.links = set()
        self.find_links()

    def find_links(self):
        soup = BeautifulSoup(self.html)
        for item in soup.find_all("a"):
            content = str(item.get('href'))
            if relative_url(content) ==True:
                url =  self.base_url + content
            elif relative_url(content) ==False:
                url =  content
            self.links.add(url)
        #return self.links
    def page_links(self):
        return self.links

#? eliminate the recursive line of code(do not repeat yourself)
#!put get_text
class PageParser:

    def __init__(self, html):
        self.soup = BeautifulSoup(html)
        self.data = dict()
        self.boot()
        self.package_data()

    def boot(self):
        self.get_title()
        self.get_author()
        self.get_summary()
        self.get_publication_date


    def get_title(self):
        article = get_article(self.soup)
        self.title = article.h2.get_text()


    def get_author(self):
        article = self.soup.find("div", {"class":"the-article"})
        self.author= article.div.span.get_text()

    def get_summary(self):
        content = self.soup.find("div", {"class":"details"})
        self.summary = content.p.get_text()

    def get_publication_date(self):
        article =self.soup.find("div", {"class":"the-article"})
        self.publication_date = article.ul.li.get_text().replace('Published:', '')

    def package_data(self):
        self.data['title'] = self.title
        self.data['author'] = self.author
        self.data['summary'] = self.summary
        self.data['publication_date'] = self.publication_date

    def page_data(self):
        return self.data
