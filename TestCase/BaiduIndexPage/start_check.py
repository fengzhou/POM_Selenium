#coding=utf-8
'''
Created on 2014��12��5��
'''
import unittest,Page
from public.public import Method

class Check(unittest.TestCase):

    def setUp(self):
        self.pb = Method()
        self.ck = Page.Check()
        self.driver = self.pb.getDriver()
        self.driver.maximize_window()
    @unittest.skipUnless(*Method.castStatus('Ready'))
    def test_01_test(self):
        u"""仅仅用于测试"""
        self.ck.open(self.driver)
        content = self.pb.getVal(1)
        self.ck.inputContent(content)
        self.ck.clickSearchButton()
        self.assertEqual(self.ck.getTitle(),u'selenium_百度搜索')
        self.ck.save_ok_pic('search')
        self.driver.close()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
