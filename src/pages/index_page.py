class Index_Page:
    def __init__(self,my_driver):
        self.loginbtn="login"
        self.driver=my_driver
        
    def click_login(self):
        
        self.driver.find_element_by_class_name(self.loginbtn).click()