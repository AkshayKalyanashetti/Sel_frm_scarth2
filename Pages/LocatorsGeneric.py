import allure
from selenium.common.exceptions import *
#import xlrd
# import os
import moment
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


class LocatorGeneric:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_element_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_element_by_xpath(locator_val)
            elif loc_type == "tagname":
                ele = self.driver.find_element_by_tag_name(locator_val)
        except NoSuchElementException as e:
            print(e)
        except ElementNotInteractableException as e:
            print(e)
        except WebDriverException as e:
            print(e)
        except NoSuchWindowException as e:
            print(e)
        except UnexpectedTagNameException as e:
            print(e)
        except ElementClickInterceptedException as e:
            print(e)
        except SessionNotCreatedException as e:
            print(e)
        except StaleElementReferenceException as e:
            print(e)
        except Exception as e:
            print(e)
        return ele


    def get_screenshot(self, log):
            cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = log + "  " + cur_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            # self.driver.get_screenshot_as_file(
            #     os.getcwd().replace("\\", "/").replace("pages", "") + "/screenshots/" + screenshot_name + ".png")
            # print(os.getcwd().replace("\\", "/").replace("tests", "screenshots") + "/" + screenshot_name + ".png")
