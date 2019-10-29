# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new group", header="asd", footer="asd"))
    app.group.return_to_group_page()
    app.group.open_groups_page()
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_group_page()
    app.session.logout()

