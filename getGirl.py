#-*-coding:utf-8-*-
#@Time:2021/1/2720:25
#@Author:陈 玉 皓
#@File:getGirl.py
#@Sofeware:PyCharm

#获取全网美女高清图
import requests
import re
import time
#1.模拟浏览器发起请求
	#地址：
url = 'https://www.huya.com/g/4079#cate-0-0'
	#发起请求：urllib  requests(第三方库)
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
}


#2.获取响应内容

response = requests.get(url=url,headers=headers)
# print(response.text)
	#爬虫：状态码不为200 全为错


#3.解析内容
	#re findall("解析规则",文件)
	#解析规则：bs4 xpath
	# .表示任意字符 * 表示零次或者多次匹配 ？限制条件，满足当前情况下，尽可能少的匹配，提升效率
img = re.findall('<img class="pic" data-original="(.*?)"',response.text)
name = re.findall('data-default-img="338x190" alt="(.*?)"',response.text)
# print(img,name)

#匹配名字和图片 zip方法  想要查看zip的内容，只能通过list解析
# print(list(zip(img,name)))
#4.保存内容
for i,n in zip(img,name):
	resq = requests.get(i)
	#保存图片 wb:以二进制形式写入
	with open("img/"+ str(n)+'.jpg','wb') as file:
		file.write(resq.content)
	print(n + "下载完成")
	# time.sleep(0.3)