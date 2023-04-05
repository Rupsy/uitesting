from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self , driver):
        self.driver = driver

    def do_click(self , by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_click_on_clickable(self , by_locator):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)))


    def do_send_key(self , by_locator , text):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self , by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self , by_locator ):
        element =  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self , title) :
        WebDriverWait(self.driver,100).until(EC.title_is(title))
        print ("title " , self.driver.title)
        return self.driver.title






