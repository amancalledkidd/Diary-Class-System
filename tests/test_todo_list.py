from lib.todo_list import TodoList

"""
create todo list instance
check check todo List initalises
"""
def test_empty_incomplete_list():
    todo_list = TodoList()
    assert todo_list.incomplete_list == []