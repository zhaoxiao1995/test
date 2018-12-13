from selenium import webdriver

class Pyselenium():
    def __init__(self,browser):
        if browser == "Chrome":
            driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        elif browser == "Edge":
            driver = webdriver.Edge()
        elif browser == "Ie":
            driver = webdriver.Ie(executable_path='./drivers/IEDriverServer')
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Opera":
            driver = webdriver.Opera()
        elif browser == "Safari":
            driver = webdriver.Safari()
        elif browser == "PhantomJS":
            driver = webdriver.PhantomJS()
        else:
            print("不存在这个浏览器，请检查后再试！")
            raise
        self.driver = driver

    def open(self,url):
        '''
        说明：打开网址
        用法：open('http://www.baidu.com')
        '''
        self.driver.get(url)
    
    def close(self):
        '''
        退出浏览器
        '''
        self.driver.quit()
    
    def get_element(self,byvalue):
        '''
        说明：定位元素
        用法：get_element('id->su')
        '''
        by = byvalue.split("->")[0]
        value = byvalue.split("->")[1]
        if by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif by == 'link':
            element = self.driver.find_element_by_link_text(value)
        else:
            print(by,value)
            raise
        return element

    def send(self,byvalue,value):
        '''
        说明：定位元素，并直接输入数据
        用法：send('id-->su','浪晋的测试小讲堂')
        '''
        element = self.get_element(byvalue)
        element.send_keys(value)