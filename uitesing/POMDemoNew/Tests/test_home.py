import time

import pytest

from POMDemoNew.Config.config import TestData
from POMDemoNew.Pages.HomePage import HomePage
from POMDemoNew.Pages.LoginPage import LoginPage
from POMDemoNew.Tests.test_base import BaseTest


class Test_Home(BaseTest):

    @pytest.mark.skip(reason="move on with next one ")
    def test_account(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)
        homePage.your_account_link_click()
        time.sleep(10)
        homePage.account_link_click()
        time.sleep(10)

    '''def test_orders(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)
        homePage.returns_and_orders()
        homePage.get_order_list()'''

    '''def test_order_for_year(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)
        homePage.returns_and_orders()
        homePage.get_order_for_year()
        time.sleep(30)'''

    @pytest.mark.skip(reason="move on with next one ")
    def test_buy_30_days_old_spiritual_bestSeller(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)
        homePage.books_click()

    @pytest.mark.skip(reason="move on with next one ")
    def test_search_and_add_book_to_cart(self):

        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)
        homePage.books_buy()
        time.sleep(10)


    def test_scroll_to_bottomof_page(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)
        homePage.scroll_down()


