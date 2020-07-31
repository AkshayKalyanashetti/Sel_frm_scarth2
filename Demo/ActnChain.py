from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
driver.maximize_window()
driver.get("http://www.actitime.com/")
action = ActionChains(driver)
ac = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/a")
ac1 = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/ul/li[1]/a")
action.move_to_element(ac).move_to_element(ac1).click().perform()