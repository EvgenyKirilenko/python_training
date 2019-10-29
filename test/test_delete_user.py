from model.user import User

def test_delete_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.test_delete_first_user()
    app.session.logout()