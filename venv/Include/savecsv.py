# 保存成csv格式
import csv
import spiderurl as combin


def savecsv(pageNum):
    # 定义一个大的列表将所有的招聘信息都放进去
    job_name = ['python', 'java', '机器学习', '数据挖掘', '深度学习', 'c++']
    # job_name = ['python']
    # 工作名字
    for job in job_name:
        # print(job)
        joblist = []
        # 将页面读取的数据保存起来
        # 每个工作的名字工作信息

        url = 'https://sou.zhaopin.com/?pageSize=60&jl=530&kw=' + job + '&kt=3'
        print("开始爬取工作："+job+"地址是："+url)

        # 拼接完成爬取文件并解析
        joblist = combin._urldata_(url, pageNum)

        # 把数据存成csv格式
        filenames = ["job_title", "company_title", "job_saray", "job_demand_info_address", "job_demand_info_age",
                     "job_demand_info_back",
                     "company_info_back", "company_info_number", "job_welfare_info_list"]
        for list in joblist:
            # 以字典的形式写入文件
            with open(job + ".csv", "a", errors="ignore", newline='') as fp:
                f_csv = csv.DictWriter(fp, fieldnames=filenames)
                f_csv.writerow(list)
