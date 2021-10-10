from selenium.webdriver.remote.webelement import WebElement

class Report:
    def __init__(self, front_page_listing: WebElement):
        self.listing = front_page_listing
        self.deals = self.pull_deals()

    def pull_deals(self):
        return self.listing.find_elements_by_class_name('s-item')

    def pull_info(self):
        deal_list = []
        counter = 1
        for ind_items in self.deals:
            title = ind_items.find_element_by_class_name('s-item__title').get_attribute('innerHTML')
            # quality = ind_items.find_element_by_class_name('s-item__subtitle').get_attribute('innerHTML')
            quality = ind_items.find_element_by_xpath(f"(//span[@class='SECONDARY_INFO'])[{counter}]")
            price = ind_items.find_element_by_class_name('s-item__price').get_attribute('innerHTML')
            deal_list.append([title, quality.text, price])
            if(counter < 51): counter += 1
        return deal_list

