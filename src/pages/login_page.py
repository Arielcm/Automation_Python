class Login_Page:
    def __init__(self,My_Driver):
        self.emailtxt="email"
        self.passtxt="passwd"
        self.loginbtn="SubmitLogin"
        self.driver=My_Driver
        
    def login(self,email,con):
        #email=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"email"))) 
        self.driver.find_element_by_id(self.emailtxt).send_keys(email)
        self.driver.find_element_by_id(self.passtxt).send_keys(con)
        self.driver.find_element_by_id(self.loginbtn).click()
        