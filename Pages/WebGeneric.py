from Pages.LocatorsGeneric import LocatorGeneric

class WebGeneric(LocatorGeneric):
    def __init__(self, driver):
        LocatorGeneric.__init__(self, driver)
        self.lc = LocatorGeneric(self.driver)

    #enter text values[locator_type, locator_val, input_val]
    #@Given Enter "INPUT VAL" "LOCATORType" and "Locator Val"
    def enter(self, locator_type, locator_val, input_val):
        var = self.locator(locator_type, locator_val)
        var.send_keys(input_val)
        self.get_screenshot("Entered " + input_val + " in text field")

        #self.get_screenshot("Entered "+input_val+" in text field")

    def submit(self, locator_type, locator_val):
        var = self.locator(locator_type, locator_val)
        var.click()
        self.get_screenshot("Entered " + locator_val + " in text field")

