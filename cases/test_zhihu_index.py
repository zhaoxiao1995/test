import unittest
from selenium import webdriver
from bao import pyselenium

class Test_zhihu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("go")
        
        cls.dirver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        cls.dirver.get("http://www.zhihu.com/signup")

    @classmethod
    def tearDownClass(cls):
        cls.dirver.quit()
        print("down")
    
    def test_zhihu_index01(self):
        self.dirver.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/div/div/div[2]/div[2]/span").click()
        self.dirver.find_element_by_name("username").send_keys("18583707821")
        self.dirver.find_element_by_name("password").send_keys("zx1995821")
        self.dirver.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/div/div/div[2]/div[1]/form/button").click()
        res = self.dirver.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/div/div[2]/div/div/div[4]/ul/li[2]/a/span").text
        self.assertEqual(res," © 2018 知乎","测试")
    
# <span class="GlobalSideBar-navText">我的收藏</span>
#<button type="submit" class="Button SignFlow-submitButton Button--primary Button--blue">登录</button>
# //*[@id="root"]/div/main/div/div/div[2]/div/div/div[4]/ul/li[2]/a/span