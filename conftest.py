import pytest
#from data.testdata import *

import os
@pytest.fixture(scope='class')#conftest will be executed
                                    # for each and every test
#@pytest.fixture(scope='class')#conftest will be executed
#                                   only one time
#@pytest.fixture(scope='session')#conftest will be
#                                   executed only one time
def test_setup(request):
    from selenium import webdriver
    dir = "C:\\Users\\Akshay\\Desktop\\Sel_frm_scarth\\Drivers"
    print(dir)
    driver = webdriver.Chrome(dir+"\\chromedriver.exe")
    driver.get("http://demo.actitime.com")
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.quit()