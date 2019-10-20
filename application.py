from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def submit_creation(self):
        wd = self.wd
        # submit creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def fill_group_create_form(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_creation(wd)

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_login_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_login_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def submit_new_user(self):
        wd = self.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        
    def fill_new_user_form(self,  user):
        wd = self.wd
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

    def open_add_user_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()