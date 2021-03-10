# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/28 10:44

from web_crawler.get_html import get_html_with_header, get_redirect_url_and_html
from bs4 import BeautifulSoup
import urllib.parse
import re
from pprint import pprint


def extract(html):
    res = []
    soup = BeautifulSoup(html, 'lxml')
    abstract_soup = soup.find('div', {'class': 'summary'})
    # print('abstract_soup:-----------', abstract_soup)
    if abstract_soup:
        abstract = abstract_soup.get_text()
        # print('abstract:-----', abstract)
    else:
        abstract = ''
        # print('abstract:-----', abstract)
    pages = set()
    for link in abstract_soup.find_all('a'):
        # print(link)
        if 'href' in link.attrs:
            # pages.add('https://baike.sogou.com'+link.attrs['href'])
            url = link.attrs['href']
            if url.startswith('http://www.baike.com/wiki/'):
                pages.add(url)

    # return abstract
    pprint(pages)
    # redirect_pages = set()
    # for page in pages:
    #     redirect_url, html = get_redirect_url_and_html(page)
    #     print(redirect_url.split(";")[0])


if __name__ == '__main__':
    from pprint import pprint

    # html = get_html('https://baike.sogou.com/v218636.htm?fromTitle=' + urllib.parse.quote('钟南山'))
    html = get_html_with_header('http://www.baike.com/wiki/%E9%92%9F%E5%8D%97%E5%B1%B1&prd=button_doc_entry')

    extract(html)
