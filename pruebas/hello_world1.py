import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    def setUp(cas):
        return super(). setUP()
        
    def test_hello_world(self):
        pass
        

    def tearDown(cls):
        return super(). tearDown()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output="reportes",report_name="hello-report"))

