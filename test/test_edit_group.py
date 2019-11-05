from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="new group", header="asd", footer="asd"))
    app.group.return_to_group_page()
    app.session.logout()