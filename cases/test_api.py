import unittest #导入unittest包 就可以用里面的东西
import requests #requests 接口测试的包

class Test_demo(unittest.TestCase):#新建一个test_demo的类继承了 包里面这个testcase这个类
    
    @classmethod
    def setUpClass(cls):
        print('测试开始')
    @classmethod
    def tearDownClass(cls):
        print('测试结束')

    def test_case_login_01(self):#登录接口测试用例01 测试正常登录成功
        url = "http://lux.itblacklist.top/userLogin/"
        payload = {"username":"test","password":"test","captcha":"123456"}
        headers = {'Content-Type':"application/json"}
        response = requests.request("POST",url,json=payload,headers=headers)
        #调用request函数跑接口 返回存在response 这个变量中
        print(response.text) 
        fanhuizhi = response.json() #这个.json()应该是一个按json格式获取数据的函数 如果是.text的话就是获取txt格式的返回数据
        res_code = fanhuizhi.get('code') #把返回的东西response的json格式看成一个字典 这里是获取字典中的值
        res_msg = fanhuizhi['msg']
        
        #断言函数   此处的函数是 （1,2，msg）判断 1 和 2 是否相等 
        self.assertEqual(res_code,200,'判断返回值中code是否正常为200')
        self.assertEqual(res_msg,'登录成功!','判断返回值中msg是否正常为登录陈宫')
        #应该可以建一个res的字典把msg和code放在一起 断言就可以只写一句 判断两个值放在一起的字典是否相同
        #就只返回一个结果  . 为用例通过 false为用例不通过

    def test_case_login_02(self):#测试密码错误的异常登录
        url = "http://lux.itblacklist.top/userLogin/"
        payload = {"username":"test","password":"zxzx","captcha":"123456"}
        headers = {'Content-Type':"application/json"}
        response = requests.request("POST",url,json=payload,headers=headers)
        print(response.text) 
        fanhuizhi = response.json() 
        res_code = int(fanhuizhi.get('code') )
        res_msg = fanhuizhi['msg']
        #断言函数  
        self.assertEqual(res_code,-100,'判断返回值中code是否正常为-100')
       #self.assertEqual(res_msg,'登录成功!','判断返回值中msg是否正常为登录陈宫')

    # def test_1_jia(self):
    #     self.assertEqual(1+1,2,'测试1+1=2')
    # def test_2_jian(self):
    #     self.assertEqual(1-1,0,'测试1-1=0')
    # def test_3_chu(self):
    #     self.assertEqual(2/1,2,'测试2/1=2')
    # def test_4_chen(self):
    #     self.assertEqual(1*2,4,'测试1*2=4')

