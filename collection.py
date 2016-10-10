#!/usr/bin/env python
#coding=utf-8
import sys, os, time, re
from api.iptocity import ipip_api
from collections import Counter

import django

pro_dir = os.getcwd()
sys.path.append(pro_dir)
os.environ['DJANGO_SETTINGS_MODULE'] ='map.settings'  #ÏîÄ¿µÄsettings
django.setup()

from dotmap.models import Pageview


daytime = time.strftime('%Y%m%d')
hourtime = time.strftime('%Y%m%d%H')
cpath = os.path.abspath(os.path.dirname(__file__))
logdir = '%s/logs/o2o/%s' % (cpath, daytime)


if not os.path.exists(logdir):
    exit()
    
logfiles = [ log for log in os.listdir(logdir) if hourtime in log.split('_')[-1] ]


ips = []

# ipre = re.compile(r'\d+\.\d+\.\d+\.\d+', re.IGNORECASE)


for log in logfiles:
    with open(os.path.join(logdir, log), "r") as f:
        for line in f.readlines():
            # iplist = re.findall(ipre, line.split()[0])
            iplist = line.split()[0]
            if iplist:
                ips.append(iplist)
                # ips.extend(iplist)

        
data = dict(Counter(ips))


# ip -> city, write in dbfile
finaldata = {}
for ip in data.keys():
    city = ipip_api(ip)
    
    if city:
        if finaldata.has_key(city):
            finaldata[city] = int(finaldata[city]) + int(data[ip])
        else:
            finaldata.setdefault(city, int(data[ip])) 

# print finaldata

for city in finaldata.keys():
    row = Pageview.objects.filter(dtime=daytime, city=city).first()
    
    if row:
        row.count = finaldata[city]
        row.save()
    else:
        sql = Pageview(dtime=daytime, city=city, count=finaldata[city])
        sql.save()
    
    



    
    
    

