from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="new group name"))
    app.group.return_to_group_page()
