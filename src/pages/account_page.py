class Accoun_Page:
    def __init__(self,My_Driver):
        self.driver=My_Driver
        
    def title_page(self):
        return self.driver.title