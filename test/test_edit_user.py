def test_edit_first_user(app):
    app.session.login(username="admin", password="secret")
    app.group.test_edit_first_group()
    app.session.logout()