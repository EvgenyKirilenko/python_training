from model.group import Group


def test_add_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.click_submit()
    app.group.return_to_group_page()
    app.session.logout()
