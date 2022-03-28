import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class DynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Dynamic Controls").click()
        
        
    def test_dinamic_controls(self):
        driver=self.driver
        check_box=driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        check_box.click()
        
        remove_add_botton=driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_botton.click()
        
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkbox-example > button")))
        remove_add_botton.click()
        
        
        enable_disable_button = driver.find_element_by_css_selector('#input-example > button:nth-child(2)')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button:nth-child(2)')))

        text_area = driver.find_element_by_css_selector('#input-example > input:nth-child(1)')
        text_area.click()
        sleep(3)
        text_area.send_keys('Hola')
        sleep(3)

        enable_disable_button.click()    
        
        
        
        
    def tearDown(self):
        self.driver.close()
        

if __name__=="__main__":
    unittest.main(verbosity=2)
    