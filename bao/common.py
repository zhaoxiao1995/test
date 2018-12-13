import xlrd #这个包可以操作excle
import pymysql #这个包操作数据库
import config #导入配置文件
import requests


def getExcel(sheetname,hang,lie):
    '''
    读取excel文件 文件名和路径在config中配置
    用法：getExcle("分页名"，行，列)
    eg：getExcle("Sheet1",0,2)
    '''
    excleName = config.testdata #导入配置表格文件 
    data = xlrd.open_workbook(excleName) #调用xlrd包的函数打开文件
    table = data.sheet_by_name(sheetname) #选择table分页
    shuju = table.cell_value(hang,lie) #选择具体行和列 坐标从0开始
    return shuju #返回表格中的数据
# a = getExcle("Sheet1",0,2)
# print(a)

def getDb(sql):
    '''
    执行sql语句并返回查询到的数据库的值
    以元组的数据类型返回
    '''
    dbinfo = config.dbinfo #数据库信息 在config中配置的
    db = pymysql.connect(**dbinfo) #连接数据库
    cursor = db.cursor() # 游标 实例化
    cursor.execute(sql) #调用函数 执行sql语句
    res = cursor.fetchall() #接住数据
    return res


def runApi(api_type,url,canshu,header_info={'Content-Type':"application/json"}):
    '''
    跑接口函数
    用法 runApi(接口类型，接口地址，传入参数，头部信息 默认为conten:app/json)
    eg:runApi("POST","http://lux.itblacklist.top/userLogin/",{"username":"test", "password":"test", "captcha":"123456"})
    '''

    response = requests.request(api_type,url,json=eval(canshu),headers=header_info)
    #调用request函数跑接口 返回存在response 这个变量中
    print(response.text) #打印返回结果
    return response.json() #return返回结果的json格式
# runApi("POST","http://lux.itblacklist.top/userRegist/",{"username":"testluxapi1", "password":"api", "nickname":"testluxapi1"})
