import requests
import json

url='https://zhihuotech.com/devj/applet/cardInfo'
header_dict={
        'charset': 'utf-8',
        'Accept-Encoding': 'gzip',
        'referer': 'https://servicewechat.com/wx358a536fed195cc8/0/page-frame.html',
        'content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MicroMessenger/7.0.9.1560(0x27000934) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
        'Content-Length': '107',
        'Host': 'zhihuotech.com',
        'Connection': 'Keep-Alive'
    }
params={'class_id':'31410007232205208',
           'role':'0',
           'student_id':'',
           'union_id':'oyu3N0X-jvsSabhqSPhCQd42yZ-A',
           'page_num':'1',
           'page_size':'10'
    }
r = requests.post(url=url,headers=header_dict,data=params,verify=True)
print(r.url)#传递url参数
print(r.text)#想要内容
print(r.status_code)#状态码
print(r.json())#json响应内容
print(r.headers)#响应头


