import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.account_page import Accoun_Page
from pages.index_page import Index_Page
from pages.login_page import Login_Page


class First_Test(unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://automationpractice.com")
        self.driver.maximize_window()
        self.index_page=Index_Page(self.driver)
        self.login_page=Login_Page(self.driver)
        self.account_page=Accoun_Page(self.driver)
       
    def test_login(self):
        self.index_page.click_login()
        self.login_page.login("practice@practice.com", "practice")
        self.assertEquals(self.account_page.title_page(),"My account - My Store")
        
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()