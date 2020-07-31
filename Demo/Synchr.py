from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://demo.actitime.com")
driver.find_element_by_xpath("//input[@id='username']").send_keys('admin')
driver.find_element_by_xpath("//input[@name='pwd']").send_keys('manager')
driver.find_element_by_xpath('//*[@id="loginButton"]/div').click()
x=driver.title
wait = WebDriverWait(driver, 20)
status = wait.until(EC.title_is(x))
print(status)
