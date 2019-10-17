# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from group import Group
from application import Application


class AddNewGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_new_group(self):
        self.login(username="admin", password="secret")
        self.fill_group_create_form(wd, Group(name="new group", header="asd", footer="asd"))
        self.logout()

    def test_add_new_empty_group(self):
            self.login (username="admin", password="secret")
            self.fill_group_create_form(wd, Group(name="", header="", footer=""))
            self.logout()


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
