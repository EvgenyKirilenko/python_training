from selenium.webdriver.support.select import Select


class UserHelper:


    def __init__(self, app):
        self.app = app


    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def create(self, user):
        wd = self.app.wd
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

    def test_delete_first_user(self):
        wd = self.app.wd
        self.open_login_page()
        # select first user
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_login_page()

    def test_edit_first_user(self):
        wd = self.app.wd
        self.open_login_page()
        # select first user
        wd.find_element_by_name("selected[]").click()
        #submit editing
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
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
        self.open_login_page()

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_login_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()