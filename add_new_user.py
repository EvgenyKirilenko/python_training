# -*- coding: utf-8 -*-
import pytest
from application import Application
from user import User

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_user(app):
    app.open_login_page()
    app.login(username="admin", password="secret")
    app.open_add_user_page()
    app.fill_new_user_form(User(firstname="firstname", lastname="lastname", middlename="middlename",
                                    nickname="nickname", title="title", company="company", address="address",
                                    home="home", mobile="mobile", work="work", fax="fax", email="email",
                                    email2="email2", email3="email3", homepage="homepage",
                                    bday="bday", bmonth="bmonth", byear="byear", aday="aday",
                                    amonth="amonth", ayear="ayear", address2="address2", phone2="phone2", notes="notes"))
    app.submit_new_user()
    app.logout()
