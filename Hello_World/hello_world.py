import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=cls.driver
        driver.implicitly_wait(10)
        
    def test_hello_world(self):
        driver=self.driver
        driver.get("https://platzi.com/")
        
    def test_visit_wikipedia(self):
        self.driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":

    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output="reportes",report_name="Hello-report"))
    
    