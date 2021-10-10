from selenium.webdriver.remote.webdriver import WebDriver

class Filters:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_color(self,wanted_color=None):
        color = self.driver.find_element_by_css_selector(f'input[aria-label*="{wanted_color}"]')
        color.click()

    def apply_lowest(self):
        default_btn = self.driver.find_element_by_css_selector('button[aria-label*="Sort selector. Best Match selected."]')
        default_btn.click()
        lowest = self.driver.find_element_by_css_selector('a[_sp*="p2351460.m4116.l5869.c4"]')
        lowest.click()
