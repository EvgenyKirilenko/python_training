class GroupHelper:

    def __init__(self, app):
        self.app = app

    def click_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_new_group_page(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.open_new_group_page()
        self.fill_form(group)
        #self.click_submit()
        #wd.find_element_by_name("submit").click()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.click_edit()
        self.fill_form(group)
        wd.find_element_by_name("update").click()

    def click_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.change_filed_value("group name", group.name)
        self.change_filed_value("group header", group.header)
        self.change_filed_value("group footer", group.footer)

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def test_delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
