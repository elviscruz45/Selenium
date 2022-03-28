import unittest
from selenium import webdriver



class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="./chromedriver")
        driver=self.driver
        driver.implicitly_wait(130)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        
    def test_new_user(self):
        driver=self.driver
	#le decimos al driver que encuentre la opción de cuenta por su Xpath y le haga click para desplegar el menu
        self.driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
    #el driver va a buscar el enlace por su texto y haga click
        self.driver.implicitly_wait(3)    
        driver.find_element_by_link_text("Log In").click()
    #creo una variable asociada al botón de crear cuenta    
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
    #validamos que el botón esté visible y habilitado    
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
    #comprueba que estamos en el sitio de crear cuenta
        self.assertEqual('Create New Customer Account', driver.title)
	#creación de variables con el nombre del selector correspondiente
        first_name = driver.find_element_by_id('firstname')
        
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        self.driver.implicitly_wait(10)
        email_address = driver.find_element_by_id('email_address')
        self.driver.implicitly_wait(13)
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')
    #veremos si los elementos están habilitados
    
        self.assertTrue(first_name.is_enabled() 
        and middle_name.is_enabled()		
        and last_name.is_enabled()
		and email_address.is_enabled()
		and password.is_enabled()
		and confirm_password.is_enabled()
		and news_letter_subscription.is_enabled()
		and submit_button.is_enabled())
    
    #mandamos los datos al formulario
        self.driver.implicitly_wait(10)
        first_name.send_keys('Test')
        self.driver.implicitly_wait(3)
        middle_name.send_keys('Test')
        self.driver.implicitly_wait(3)
        last_name.send_keys('Test')
        self.driver.implicitly_wait(3)
        email_address.send_keys('arqcftlothxuknlxkt@awdrt.com')
             
    #sacado de 10-minute mail     
        self.driver.implicitly_wait(3)
        password.send_keys('Test')
        self.driver.implicitly_wait(3)
        confirm_password.send_keys('Test')
        self.driver.implicitly_wait(3)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(1300)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)