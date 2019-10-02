# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_login_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_user_page(wd)
        self.fill_new_user_form(wd)
        self.submit_new_user(wd)
        self.logout(wd)

    def submit_new_user(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_login_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def fill_new_user_form(self, wd):
        wd.find_element_by_name("firstname").send_keys("firstname")
        wd.find_element_by_name("middlename").send_keys("middle name")
        wd.find_element_by_name("lastname").send_keys("last name")
        wd.find_element_by_name("nickname").send_keys("nickname")
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").send_keys("home")
        wd.find_element_by_name("mobile").send_keys("mobile")
        wd.find_element_by_name("work").send_keys("work")
        wd.find_element_by_name("fax").send_keys("fax")
        wd.find_element_by_name("email").send_keys("email")
        wd.find_element_by_name("email2").send_keys("email2")
        wd.find_element_by_name("email3").send_keys("email3")
        wd.find_element_by_name("homepage").send_keys("homepage")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").send_keys("1999")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").send_keys("address")
        wd.find_element_by_name("phone2").send_keys("home")
        wd.find_element_by_name("notes").send_keys("notes")

    def open_add_user_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
