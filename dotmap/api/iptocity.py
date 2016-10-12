#coding=utf-8

import sys, os, urllib, urllib2, hashlib, json
reload(sys)
sys.setdefaultencoding('utf-8')
from ipip import IP

# 淘宝接口，每秒10次
def taobao_api(ip):
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" %ip
    content = urllib2.urlopen(apiurl).read()
    data = json.loads(content)['data']
    code = json.loads(content)['code']

    if code == 0:   # success
        city = data['city'].replace('市','')
        return city
        
# 百度接口，通过接口算法调用。每天10W次    
def baidu_api(ip):
    # ip = '202.96.209.5'
    ak = '4Z9Yz5Tj1thfGEkWZQGlEqj7Y3w9AAHz'
    sk = 'CLD8fIpZn4Ns5o9xqd86ND4dIlyFyyFD'

    # queryStr decoded，safe words were preserved.
    queryStr = '/location/ip?ak=%s&ip=%s' % (ak, ip)
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodedStr + sk
    sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()

    ipapi = 'http://api.map.baidu.com/location/ip?ak=%s&ip=%s&sn=%s' % (ak, ip, sn)
     
    res = urllib2.urlopen(ipapi)
    data = json.loads(res.read())
    
    if data['status'] == 0:
        # city = data['content']['address_detail']['city'].replace('市','')
        city = data['address'].split('|')[2]
    else:
        city = u'unknow'

    return city
    
# ipip.cn本地免费地址库，准确性低。速度快
def ipip_api(ip):
    
    dbpath = os.path.join(os.path.dirname(__file__),"17monipdb.dat")
    
    IP.load(dbpath)
    
    try:
        city = IP.find(ip).split()[2]
        return city
    except:
        pass
    
        
    
    
if __name__ == '__main__':

    # IP地址为参数
    ip = sys.argv[1]
    
    print ip
    
    if ip:
        c = ipip_api(ip)
        print u'City：%s' % c
        
        
    
    
    
    
    
    
    
    
    