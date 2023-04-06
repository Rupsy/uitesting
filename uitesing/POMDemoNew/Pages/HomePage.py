import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from POMDemoNew.Pages.BasePage import BasePage


class HomePage(BasePage):

    ACCOUNT_LIST_DROPDOWN = (By.XPATH , "//header/div[@id='navbar']/div[@id='nav-belt']/div[3]/div[1]/a[2]/span[1]/span[1]")
    YOUR_ACCOUNT_LINK   = (By.XPATH , "//span[contains(text(),'Your Account')]")
    YOUR_ORDERS_LINK   = (By.XPATH , "//span[contains(text(),'Your Orders')]")
    YOUR_WISHLIST_LINK = (By.XPATH , "//span[contains(text(),'Your Wish List')]")
    YOUR_RECOMMENDATIONS = (By.XPATH , "//span[contains(text(),'Your Recommendations')]")
    YOUR_PRIME_MEMBERSHIP = (By.XPATH , "//span[contains(text(),'Your Prime Membership')]")
    RETURNS =(By.XPATH , "//span[contains(text(),'Returns')]")
    ORDER_LIST = (By.XPATH , "//div[@class='order-card js-order-card']")
    PAGINATION = (By.XPATH , "//div[@class='a-text-center']/descendant::*/li")
    ORDER_DURATION= (By.CSS_SELECTOR , "#a-autoid-1-announce")
    ORDER_DURATION_LIST = (By.XPATH , "//ul[@class='a-nostyle a-list-link']/descendant::li")
    BOOKS = (By.XPATH , "//header/div[@id='navbar']/div[@id='nav-main']/div[2]/div[2]/div[1]/a[9]")
    BOOKS_LAST_30_DAYS = (By.XPATH , "//span[contains(text(),'Last 30 days')]")
    BOOKS_LAST_90_DAYS = (By.XPATH , "//span[contains(text(),'Last 90 days')]")

    BOOKS_NEXT_90_DAYS = (By.XPATH , "//span[contains(text(),'Next 90 days')]")
    BOOKS_RELIGION_AND_SPIRITUALITY = (By.XPATH , "//span[contains(text(),'Religion & Spirituality')]")
    BOOKS_BEST_SELLER = (By.XPATH , "//span[contains(text(),'Best seller')]")
    BOOKS_PAGINATION = (By.XPATH , "//div[@class='s-pagination-strip']/descendant::span")
    BOOK_ITEMS = (By.XPATH , "//div[@class='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16']")
    SEARCH = (By.ID , "twotabsearchtextbox")
    SEARCH_ENTER = (By.XPATH , "//input[@id='nav-search-submit-button']")
    ADD_TO_CART = (By.ID , "//input[@id='add-to-cart-button']")
    IKIGAI = (By.XPATH , "//span[contains(text(),'Ikigai : Japanese Art of staying Young.. While growing Old')]")





    def __init__(self,driver):
        super().__init__(driver)

    def your_account_link_click(self):
        self.do_click(self.ACCOUNT_LIST_DROPDOWN)


    def account_link_click(self):
        self.do_click(self.YOUR_ACCOUNT_LINK)

    def your_orders(self):
        self.do_click(self.YOUR_ORDERS_LINK)

    def your_wishlist(self):
        self.do_click(self.YOUR_WISHLIST_LINK)

    def your_recommendations(self):
        self.do_click(self.YOUR_RECOMMENDATIONS)


    def your_prime_membership(self):
        self.do_click(self.YOUR_PRIME_MEMBERSHIP)

    def returns_and_orders(self):
        self.do_click(self.RETURNS)

    def get_order_for_year(self):
        self.do_click_on_clickable(self.ORDER_DURATION)

        duration_lists = self.driver.find_elements(By.XPATH , "//ul[@class='a-nostyle a-list-link']/descendant::li")
        for duration in duration_lists:

            if duration.text == "2023":
                print("TEXT ---", duration.text)
                duration.click()

    def get_order_list(self):

        pages= self.driver.find_elements(By.XPATH ,"//div[@class='a-text-center']/descendant::*/li" )
        url_list = []
        pagenum = 0
        retry = 0
        for page in pages:
            pagenum = pagenum + 1
            url_list.append(self.driver.current_url)
            self.driver.implicitly_wait(4)
            click_next = self.driver.find_element(By.CLASS_NAME , 'a-last').click()
            print("Page " + str(pagenum) + " grabbed")
            try:
                elements = self.driver.find_elements(By.XPATH ,"//div[@class='order-card js-order-card']" )
                print("Size ", elements)
                list_pdt = []
                for element in elements:
                    print ("Product detail " , element.text)
                    list_pdt.append(element.text)
            except  Exception :
                print(Exception)
            print ("Element grabbed from all pages " , list_pdt)

    def books_click(self):
        self.do_click(self.BOOKS)
        self.do_click((self.BOOKS_LAST_30_DAYS))
        self.do_click(self.BOOKS_RELIGION_AND_SPIRITUALITY)

        pages= self.driver.find_elements(By.XPATH ,"//span[@class='s-pagination-strip']/descendant::span")
        url_list = []
        pagenum = 0
        retry = 0
        print("I m here " , pages)
        for page in pages:
            pagenum = pagenum + 1
            url_list.append(self.driver.current_url)
            self.driver.implicitly_wait(4)
            page.click()
            time.sleep(10)
            print("Page " + str(pagenum) + " grabbed")

    def books_buy(self):
        self.do_click(self.BOOKS)
        self.do_send_key( self.SEARCH, "Ikigai")
        self.do_click(self.SEARCH_ENTER)
        books = self.driver.find_elements(By.XPATH ,"//div[@class='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16']" )
        txt = "Ikigai: The Japanese secret to a long and happy life"
        not_needed_txt = "Transform Your Life with Robin Sharma"
        for book in books:
            self.driver.implicitly_wait(4)
            print("book.text >>>>", book.text)
            if txt in book.text and txt not in not_needed_txt:
                print(".text @@@!!!!@@", book.text)
                print("book.text @@@@@", book.text)
                self.driver.implicitly_wait(4)

                click_next = self.driver.find_element(By.XPATH , "//span[@class='a-size-medium a-color-base a-text-normal']").click()
                #book.click()
                time.sleep(10)
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(10)
                self.do_click(self.ADD_TO_CART)
