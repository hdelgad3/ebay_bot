from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.Filters import Filters
import os
from src.reports import Report
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import os

class Item(webdriver.Chrome):
    def __init__(self, driverP = r"C:/Users/17204/Desktop/item_query", sd=False):
        self.sd = sd
        self.driverP = driverP
        os.environ['PATH'] += self.driverP
        super(Item, self).__init__()
        self.implicitly_wait(10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sd:
            self.quit()

    def get_page(self):
        self.get("https://www.ebay.com")

    def search_val(self):
        search_field = self.find_element_by_id('gh-ac')
        search_field.clear()
        search_field.send_keys("Sony WH-1000XM4 Noise Cancelling Wireless Headphones")

    def category(self):
        cat_drop = self.find_element_by_id('gh-cat')
        cat_drop.click()
        spec_cat = self.find_element_by_css_selector('option[value*="293"]')
        spec_cat.click()


    def submit_btn(self):
        btn = self.find_element_by_id('gh-btn')
        btn.click()

    def apply_filters(self):
        filt = Filters(driver=self)
        wanted_color = "Black"
        filt.apply_color(wanted_color)
        filt.apply_lowest()

    def report_listings(self):
        deals_container = self.find_element_by_id('srp-river-results')
        deals = Report(deals_container)
        info = deals.pull_info()
        # for single in info:
        #     print(single)
        self.generate_mail(info)

    def generate_mail(self, arr):
        SERVER = 'smtp.gmail.com'
        PORT = 587
        load_dotenv()
        FROM = os.environ.get('FROM')
        TO = os.environ.get('TO')
        PASS = os.environ.get('PASS')

        msg = MIMEMultipart()

        msg['Subject'] = 'Sony XM4 Listings Today'

        msg['From'] = FROM
        msg['To'] = TO
        table = self.create_table(arr)
        msg.attach(MIMEText(table, 'html'))
        print(table)

        server = smtplib.SMTP(SERVER, PORT)
        server.set_debuglevel(0)  # gives us error messages
        server.ehlo()  # hello handshake
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, TO, msg.as_string())

        server.quit()

    def create_table(self, arr):
        table = "<table>\n"
        headers = ["Product", "Quality", "Price"]
        table += "<tr>\n"
        for i in range(len(headers)):
            table += f"  <th>{headers[i]}</th>\n"
        table += "</tr>\n"

        # iterate through the 2d array
        for listing in arr:
            table += "<tr>\n"
            for i in listing:
                table += f"  <td>{i}</td>\n"
            table += "</tr>\n"
        table += "</table>\n"

        return table

