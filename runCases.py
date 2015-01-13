#coding=utf-8
''''''
import time
import unittest

import sys
from public import HTMLTestRunner
reload(sys)
sys.path.append('.')
sys.setdefaultencoding('utf8')  # @UndefinedVariable

listcases = ".\\TestCase"
def getAllCases():
    testunit = unittest.TestSuite()
    discovery = unittest.defaultTestLoader.discover(listcases,
                                                    pattern='start_*.py',
                                                    top_level_dir=None)
    for testsuits in discovery:
        for testcase in testsuits:
            testunit.addTests(testcase)
    return testunit

if __name__ =='__main__':
    alltestcase = getAllCases()
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    filename = '.\\report\\'+now_time+r"result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title = u'MyAutoTest',
                                           description=u'The Result')
    
    runner.run(alltestcase)
