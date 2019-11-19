# -*- coding: utf-8 -*-
from model.user import User


def test_add_new_user(app):
    app.user.open_add_new_page()
    app.user.create(User(firstname="firstnameq", lastname="lastname", middlename="middlename",
                         nickname="nickname", title="title", company="company", address="address",
                         home="home", mobile="mobile", work="work", fax="fax", email="email",
                         email2="email2", email3="email3", homepage="homepage",
                         bday="bday", bmonth="bmonth", byear="byear", aday="aday",
                         amonth="amonth", ayear="ayear", address2="address2", phone2="phone2", notes="notes"))
    app.user.click_submit()
    app.user.return_to_home_page()
