from Pages.WebGeneric import WebGeneric
class HomePage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.drpicon_btn_id= "//*[@id='topnav']/tbody/tr[1]/td[7]/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/div[1]/div/div[1]/div/div"
        self.clndr_btn_xpath='//*[@id="popup_menu_calendar"]/div[2]/div/ul/li[2]/a/div[1]'
        self.wg=WebGeneric(self.driver)

    def Home_login(self):
        # Logint to application - section 2 >>S2
        #self.driver.find_element_by_id("username").send_keys("admin")
        #un= self.wg.get_val("Login","UserName")

        #self.driver.find_element_by_name("pwd").send_keys("manager")
        self.wg.submit("id", self.drpicon_btn_id)
        self.wg.submit("xpath", self.clndr_btn_xpath)
        #self.wg.submit("xpath", self.config_repo_btn_xpath)

