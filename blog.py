# -*-coding:utf-8-*-
# @Time:2022/8/1015:40
# @Author:陈 玉 皓
# @File:blog.py
# @Sofeware:PyCharm

from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By



# 博客所有url的列表
url_list = []

global driver


def get_url(url):
    '''
    爬取当前网站所有博客的url
    :param url:
    :return:
    '''
    driver.get(url)
    # 获取当前博客页面的所有博客的link标签
    child_hrefs = driver.find_elements(By.XPATH, "//article/link")
    for child_href in child_hrefs:
        # 每个博客的链接
        href = child_href.get_attribute("href")
        print("当前爬取的博客链接为：", href)
        # 将链接存入url列表
        url_list.append(href)
        # time.sleep(1)


def add_page_view(url_list):
    '''
    每个博客增添十个访问量
    :param url_list:
    :return:
    '''
    for url in url_list:
        for i in range(10):
            driver.get(url)
            time.sleep(3)
if __name__ == '__main__':
    #######################收集阶段#######################
    # 博客首页页面
    base_url = "https://www.kdy.icu/"

    # 获取驱动
    driver = webdriver.Chrome(service=Service(r'd:\chromedriver.exe'))
    #爬取首页博客页面
    get_url(base_url)

    #根据i的不同，爬取不同页面的博客，当前为2-13页的
    for i in range(2, 14):
        url = base_url + "page/%d/" % (i)
        print("正在爬取第", i, "页的博客地址")
        get_url(url)
        print("当前集合中已经爬取了", len(url_list), "篇博客的链接~")

    print('链接收集结束，当前url集合为：', url_list)

    #######################收集阶段#######################

    add_page_view(url_list)