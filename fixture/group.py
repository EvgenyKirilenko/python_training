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

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        wd.find_element_by_name("update").click()

    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def test_delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
