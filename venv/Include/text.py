# 爬取文章
import requests
from lxml import etree
from selenium import webdriver
import time, random
from pyquery import PyQuery as pq
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def _urldata_(url, pageNum):
    # 新版本不支持phantomjs
    # browser = webdriver.PhantomJS()
    # 采用浏览器自带的无头浏览器进行查询
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    # 睡觉一秒
    time.sleep(1)
    browser.get(url)

    # # 定义一个大的列表将一个职位所有的招聘信息都放进去
    joblist = []
    # 点击下一页进行访问页面
    for i in range(1, pageNum+1):
        # 对动态网页查询并使用pyquery进行分析
        doc = pq(browser.page_source)
        # 获取一个多个相同属性
        html = doc('[class="listItemBox clearfix"]').items()
        print(html)

        listSum = []
        # 获取单个属性
        for tb in html:
            # 定义一个空字典，用于储存数组
            item = {}
            # 提取岗位
            job_title_info = tb('.job_title')
            job_title = job_title_info.attr('title')
            # 获取公司名
            company_title = tb('.company_title').text()
            # 获取薪资
            job_saray = tb('.job_saray').text()
            # 获取地址，工作要求年限，学历
            job_demand = tb('.demand_item').items()

            job_demand_info = []
            for job in job_demand:
                job_demand_info.append(job.text())

            # 获取企业名称以及企业人数
            commpanyDesc = tb('.info_item').items()

            company_info = []
            for job in commpanyDesc:
                company_info.append(job.text())

            # 获取更详细的信息
            job_welfare = tb('.welfare_item').items()

            job_welfare_info = []
            for job in job_welfare:
                job_welfare_info.append(job.text())

            job_welfare_info_list = "|".join(job_welfare_info)

            # 填入数组
            item['job_title'] = job_title
            item['company_title'] = company_title
            item['job_saray'] = job_saray
            item['job_demand_info_address'] = job_demand_info[0]
            item['job_demand_info_age'] = job_demand_info[1]
            item['job_demand_info_back'] = job_demand_info[2]
            item['company_info_back'] = company_info[0]
            item['company_info_number'] = company_info[1]
            item['job_welfare_info_list'] = job_welfare_info_list

            listSum.append(item)
            print("数据" + listSum)

        # 将所有的页面的内容进行保存
        joblist += listSum
        browser.find_elements_by_class_name('btn-pager')[1].click()
        print("爬取第" + str(i) + "页")
        print("数据共" + str(len(listSum)) + "条")
        # 防止被和谐
        p = random.randint(1, 4)
        time.sleep(p)

    return joblist

# _urldata_('https://sou.zhaopin.com/?pageSize=60&jl=530&kw=python&kt=3')
