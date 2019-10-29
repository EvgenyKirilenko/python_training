def test_edit_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.test_edit_first_user()
    app.session.logout()