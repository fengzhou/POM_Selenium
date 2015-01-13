#coding=utf-8
'''
Created on 2014��12��5��

'''
from public import Base
import time

class Check(Base.Action):
    
    def inputContent(self,content):
        loc = self.pb.getLoc(u'搜索输入框')
        self.find_element(*loc).send_keys(content)

    def clickSearchButton(self):
        loc = self.pb.getLoc(u'确定')
        self.find_element(*loc).click()
        time.sleep(2)

    def getTitle(self):
        return self.driver.title