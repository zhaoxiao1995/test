import unittest
from bao import common

class Test_Lux_api(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")

    def test_01_regist(self):
        apitype = common.getExcel("Sheet1",0,0) #获取excel中的测试数据
        url = common.getExcel("Sheet1",0,1)   
        canshu = common.getExcel("Sheet1",0,2)
        #print(apitype,url,canshu)


        responce = common.runApi(apitype,url,canshu) #调用跑接口的函数传入测试数据
        res_code = responce.get("code") #获取返回的状态码
        self.assertEqual(res_code,200,"测试注册成功")
        data = eval(canshu) #把excel中取到的参数 从字符串转为字典
        key = list(data.keys()) #获取excel字典中的key值列表
        A = key[0]  #这也可以不拆成ABC 拆成变量后面就没那么长
        B = key[1]
        C = key[2]
        #获取excel中参数部分 把字串转成字典 拆成K列表和V列表 这一部分后续可以封装起来写活 现在只能测三个参数的接口 可以封装用len()写活
        excel_value = list(data.values()) #获取excel中传入参数的值 以列表形式
        Dbdata = common.getDb('select {0},{1},{2} from tbl_user where {0} = "{3}"'.format(A,B,C,excel_value[0]))#把excel中的参数列表放进sql中查询这几个字段（参数）
        Dbdata = list(Dbdata[0]) #把查询结果转为列表...因为操作数据库返回的是元组 所以先[0]一下把二维变成一维 然后把元组转为列表

        self.assertEqual(Dbdata,excel_value,'测试数据库中的数据和预期是否一样') #对比数据库中生成的实际结果 和 excel中传入的传输 也就是预期结果
        
        
