# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_create_form(wd, Group(name="new group", header="asd", footer="asd"))
    app.logout()


def test_add_new_empty_group(app):
    app.login (username="admin", password="secret")
    app.fill_group_create_form(wd, Group(name="", header="", footer=""))
    app.logout()

