import unittest
import requests

#登录到首页页面
class TestLogin(unittest.TestCase):

    def setUp(self):
        #登录到首页所有链接
        self.url_cardInfo='https://zhihuotech.com/devj/applet/cardInfo'
        print ('开始执行用例')

    #登录到首页选择学校和任课教师班级页面
    def test_login(self):
        header1 = {
            'charset': 'utf-8',
            'Accept-Encoding': 'gzip',
            'referer': 'https://servicewechat.com/wx358a536fed195cc8/0/page-frame.html',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MicroMessenger/7.0.9.1560(0x27000934) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
            'Content-Length': '107',
            'Host': 'zhihuotech.com',
            'Connection': 'Keep-Alive'
        }
        dates1 = {'class_id': '31410007232205208',
                  'role': '0',
                  'student_id': '',
                  'union_id': 'oyu3N0X-jvsSabhqSPhCQd42yZ-A',
                  'page_num': '1',
                  'page_size': '10'
                  }
        r = requests.post(url=self.url_cardInfo, headers=header1, data=dates1, verify=True)
        resuit = r.json()
        print(r.text)

        self.assertEqual(resuit['code'],0,'首页接口失败')
        self.assertEqual(resuit['msg'],'成功','首页接口失败')
        self.assertTrue('31410007232205208' in r.text,'首页接口失败')

if __name__=='__main__':
    unittest.main()