import time

from selenium.webdriver.common.by import By

from POMDemoNew.Config.config import TestData
from POMDemoNew.Pages.BasePage import BasePage
from POMDemoNew.Pages.HomePage import HomePage


class LoginPage(BasePage):
    CLICK_SIGN_LINK= (By.XPATH , "//span[@class='nav-line-2 ']")
    SELECT_SIGN_IN = (By.XPATH , "//span[@class='a-icon a-accordion-radio a-icon-radio-active']")
    USERNAME = (By.ID , "ap_email")
    CONTINUE = (By.XPATH , "//input[@class='a-button-input'][1]")
    PASSWORD = (By.XPATH , "//input[@id='ap_password']")
    LOGIN = (By.XPATH , "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    SIGNIN = (By.XPATH , "//input[@id='signInSubmit']")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    def get_login_page_title(self ,  title):
        text = self.get_title(title)
        return text

    def is_login_Link_visible(self , login):
        self.is_enabled(login)

    def do_login(self , unae , passwd):

        self.do_click(self.CLICK_SIGN_LINK)
        self.do_send_key(self.USERNAME , "ashekhar@gmail.com")
        self.do_click(self.CONTINUE)
        self.do_send_key(self.PASSWORD , TestData.PASSWORD)
        self.do_click(self.SIGNIN)
        return HomePage(self.driver)


