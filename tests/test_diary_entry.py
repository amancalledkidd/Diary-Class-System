from lib.diary_entry import *

"""
Check DiaryEntry stores title and contents
"""
def test_format():
    first_entry = DiaryEntry("Hi", "Welcome")
    assert first_entry.format() == 'Hi: Welcome'

"""
add entry
Check word count
return count
"""
def test_word_count():
    first_entry = DiaryEntry("Hi", "Welcome")
    assert first_entry.word_count() == 1

"""
create entry with phone num
search for phone num
check if correct list is returned
"""
def test_phone_num_search():
    first_entry = DiaryEntry("Hi", "07949846018")
    assert first_entry.phone_num_search() == ["07949846018"]

# """
# Create entry with todo
# call todo search
# return todo list
# """
# def test_todo_search():
#     first_entry = DiaryEntry("Hi", "#TODO Go for run")
#     assert first_entry.todo_search() == ['Go for run']