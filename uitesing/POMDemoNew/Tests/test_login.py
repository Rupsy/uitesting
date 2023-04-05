import time

import pytest

from POMDemoNew.Config.config import TestData
from POMDemoNew.Pages.LoginPage import LoginPage
from POMDemoNew.Tests.test_base import BaseTest


class Test_Login(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME , TestData.PASSWORD)





