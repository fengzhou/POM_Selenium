#coding=utf-8
'''
Created on 2014��12��5��

'''
from selenium.webdriver.support.wait import WebDriverWait
from public import Method
import time
import os
class Action(object):
    def __init__(self):
        self.pb= Method()
        # self.driver = None

    def open(self,driver):
        self.driver = driver
        url = self.pb.getUrl()
        self.driver.get(url)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,15).until(lambda driver :driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素" % (self,loc)
            self.save_error_pic('find_element')

    def find_elements(self, *loc):
        #return self.driver.find_element(*loc)
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)
            self.save_error_pic('find_elements')


    def save_ok_pic(self,name):
        '''保存成功截图方法'''
        try:
            time.sleep(1)
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = '.\\report\\image\\%s-%s-ok.png' % (name, now)
            print '截图保存路径为:\n%s' % os.path.abspath(pic_path)
            self.driver.get_screenshot_as_file(pic_path)
        except:
            print u'保存截图失败'

    def save_error_pic(self,name):
        '''保存失败截图方法'''
        try:
            time.sleep(1)
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = '.\\report\\image\\%s-%s-error.png' % (name, now)
            print '截图保存路径为:\n%s' % os.path.abspath(pic_path)
            self.driver.get_screenshot_as_file(pic_path)
        except:
            print u'保存截图失败'
