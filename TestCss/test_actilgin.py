from selenium import webdriver
from Pages.test_Login import LoginPage
from Pages.taskPage import TaskPage
from Pages.ReportPage import RepoPage
from Pages.homepage import HomePage
import pytest

@pytest.mark.usefixtures("test_setup")
class  TestLogin:
    def test_login(self):
        driver=self.driver
        lp=LoginPage(driver)
        lp.acti_login()

    def test_task(self):
        driver = self.driver
        tp = TaskPage(driver)
        tp.task_login()

    @pytest.mark.skip
    def test_report(self):
        driver = self.driver
        rp = RepoPage(driver)
        rp.Report_login()

    def test_home(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.Home_login()

