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
        self.click_submit()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.click_edit()
        self.fill_form(group)
        wd.find_element_by_name("update").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.click_edit()
        self.fill_group_form(new_group_data)
        self.return_to_group_page()

    def click_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)
        wd.find_element_by_name("update").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
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
