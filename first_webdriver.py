from selenium import webdriver
import unittest
import HTMLTestRunner
import sysfrom
import sleep

reload(sys)
sys.setdefaultencoding("utf-8")

class BaiduTest(unittest.TestCase):
    """"百度首页搜索测试用例"""
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = u"http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver  print u"开始[case0001]百度搜索"
        driver.get(self.base_url)
        #验证标题
        self.assertEquals(dr)