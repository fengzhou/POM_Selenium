#coding=utf-8
'''
Created on 2014年12月5日

'''
import time,xlrd,os
from selenium import webdriver
class Method:
    
    def __init__(self):
        self.path = ".\\data\\data.xls"
        self.data = xlrd.open_workbook(self.path)
    
    #获取浏览器类型
    def getBrowserType(self):
        table = self.data.sheet_by_name('Base')
        browserType = str(table.row_values(1)[1])
        return browserType

    #获取url
    def getUrl(self):
        table = self.data.sheet_by_name('Base')
        url = str(table.row_values(2)[1])
        return url

    #返回driver
    def getDriver(self):
        driver = None
        browserType = self.getBrowserType()
        if browserType == 'ie':
            driver = webdriver.Ie()
        elif browserType =='chrome':
            driver = webdriver.Chrome()
        elif browserType =='firefox':
            driver = webdriver.Firefox()
        return driver

    #获取元素定位方式
    def getLoc(self,val):
        table = self.data.sheet_by_name('element')
        rows = table.nrows
        for i in range(0,rows):
            if val in table.row_values(i):
                return tuple(table.row_values(i)[1:3])

    #获取excel中的值
    def getVal(self,val):
        table = self.data.sheet_by_name('data')
        rows = table.nrows
        for i in range(0,rows):
            if val == table.row_values(i)[0]:
                return table.row_values(i)[1]

            
    @staticmethod
    def castStatus(status):
        defautl_status = ['Design','Implement','Review','Ready','Suspend']
        if status not in defautl_status:
            return (False,'Name Error')
        else:
            if (status == 'Design' or status == 'Suspend' or status == 'Review'):
                return (False,'Case Not Ready')
            else:
                return (True,'Run Case')
            
            
