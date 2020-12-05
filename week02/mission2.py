# !/bin/python encoding=utf-8
# -*- coding: UTF-8 -*-
import requests
import csv
from lxml import etree
from time import sleep
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://www.smzdm.com/'

def get_url_name(myurl=myurl):
	response = requests.get(myurl,headers=header)

	# print(f'返回码是:{response.status_code}')
	selector = etree.HTML(response.text)

	# 商品名称列表           
	item_title = selector.xpath('//*[@id="feed-main-list"]/li/div/div[2]/h5/a/text()')

	# 商品链接列表
	item_content = selector.xpath('//*[@id="feed-main-list"]/li/div/div[2]/div[3]/a/@href')

	# 遍历关系对应字典
	item_info = dict(zip(item_title,item_content))

	for i in item_info:
    	# str.lstrip
		temp = i.split('\n')[1].lstrip()
		print(f'商品名称:{temp}\t\t\t商品链接:{item_info[i]}')

	# 保存到CSV
	# with open('data.csv', 'a', newline='',encoding='utf-8') as f:
	# 	f.write(result)
	# print(response.text)
	

if __name__=="__main__":
	
	get_url_name()

