from Pages.WebGeneric import WebGeneric
class RepoPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.reports_btn_id= "container_reports"
        self.NewRep_btn_xpath="//span[contains(text(),'New Report')]"
        self.config_repo_btn_xpath="//div[contains(text(),'Configure Report Parameters')]"
        self.wg=WebGeneric(self.driver)

    def Report_login(self):
        # Logint to application - section 2 >>S2
        #self.driver.find_element_by_id("username").send_keys("admin")
        #un= self.wg.get_val("Login","UserName")

        #self.driver.find_element_by_name("pwd").send_keys("manager")
        self.wg.submit("id", self.reports_btn_id)
        self.wg.submit("xpath", self.NewRep_btn_xpath)
        self.wg.submit("xpath", self.config_repo_btn_xpath)

