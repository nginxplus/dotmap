#!/usr/bin/env python
#coding=utf-8
import sys, os, time, re
from dotmap.api.iptocity import ipip_api
from collections import Counter


# 外部调用django的ORM
import django
pro_dir = os.getcwd()
sys.path.append(pro_dir)
os.environ['DJANGO_SETTINGS_MODULE'] ='map.settings'
django.setup()

from dotmap.models import Pageview

# 日期字符串
daytime = time.strftime('%Y%m%d')
hourtime = time.strftime('%Y%m%d%H')

# access_2016101008.log 所在路径
cpath = os.path.abspath(os.path.dirname(__file__))
logdir = '%s/logs/o2o/%s' % (cpath, daytime)


if not os.path.exists(logdir):
    exit()

# 检索当日日志文件
logfiles = [ log for log in os.listdir(logdir) if hourtime in log.split('_')[-1] ]

# 所有IP
ips = []



# 采集日志中所有的IP
# 正则表达式（尽量不用），这里采集每行第一列
# ipre = re.compile(r'\d+\.\d+\.\d+\.\d+', re.IGNORECASE)
# 数据格式：
# {'59.49.46.137': 5, '220.181.51.81': 1, '125.70.58.33': 45}


for log in logfiles:
    with open(os.path.join(logdir, log), "r") as f:
        for line in f.readlines():
            # 正则匹配IP
            # iplist = re.findall(ipre, line.split()[0])
            iplist = line.split()[0]
            if iplist:
                ips.append(iplist)
                # ips.extend(iplist)

# 统计IP的数量
data = dict(Counter(ips))

# print data

# IP查询地理位置，再次进行统计
finaldata = {}
for ip in data.keys():
    city = ipip_api(ip)
    
    if city:
        if finaldata.has_key(city):
            finaldata[city] = int(finaldata[city]) + int(data[ip])
        else:
            finaldata.setdefault(city, int(data[ip])) 

# print finaldata

# 将结果写入DB
for city in finaldata.keys():
    row = Pageview.objects.filter(dtime=daytime, city=city).first()
    
    if row:
        row.count = finaldata[city]
        row.save()
    else:
        sql = Pageview(dtime=daytime, city=city, count=finaldata[city])
        sql.save()
    
    



    
    
    

