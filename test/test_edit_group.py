from model.group import Group


def test_edit_group_name(app):
    app.group.open_groups_page()
    app.group.select_first_group()
    app.group.click_edit()
    app.group.fill_group_form(Group(name="new groupq"))
    app.group.open_groups_page()

def test_edit_group_header(app):
    app.group.open_groups_page()
    app.group.select_first_group()
    app.group.click_edit()
    app.group.fill_group_form(Group(header="new headerq"))
    app.group.return_to_group_page()


def test_edit_group_footer(app):
    app.group.open_groups_page()
    app.group.select_first_group()
    app.group.click_edit()
    app.group.fill_group_form(Group(footer="new footerq"))
    app.group.return_to_group_page()
