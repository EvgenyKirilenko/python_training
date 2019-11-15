from model.group import Group


def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_group_form(Group(name="new group"))
    app.group.return_to_group_page()
    app.session.logout()


def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="new header"))
    app.group.return_to_group_page()
    app.session.logout()


def test_edit_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="new footer"))
    app.group.return_to_group_page()
    app.session.logout()
