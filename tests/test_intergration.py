from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.todo import Todo
from lib.todo_list import TodoList

"""
Given a diary
When we add two entries
We see those entries reflected in the entries list
"""
def test_diary_add():
    my_diary = Diary()
    entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, exciting times')
    entry_two = DiaryEntry('Round 2' , 'Day two and I still lobve my diary')
    my_diary.add(entry_one)
    my_diary.add(entry_two)
    assert my_diary.list_entries() == [entry_one, entry_two]

"""
Given a diary
when two entries are added
when both entries have phone numbers
return a list of those phone numbers
"""
def test_get_phone_nums():
    my_diary = Diary()
    entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, my number is 07946464535 exciting times')
    entry_two = DiaryEntry('Round 2' , 'Day two and I still lobve my diary 07956289016')
    my_diary.add(entry_one)
    my_diary.add(entry_two)
    entry_one.phone_num_search()
    entry_two.phone_num_search()
    assert my_diary.get_phone_nums() == ['07946464535', '07956289016']

# """
# Given diary
# When two entries are added with todos
# return list of incomplete todos
# """
def test_diary_entry_todo():
    my_diary = Diary()
    my_todo_list = TodoList()
    workout = Todo('Workout')
    my_todo_list.add(workout)
    
    assert my_diary.get_todo(my_todo_list) == [workout]

"""
given a diary
when the diary has three entries
returns a entry that will be readble within given time and read_speed
"""
def test_bitsize_entry():
    my_diary = Diary()
    entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, exciting times')
    entry_two = DiaryEntry('Round 2' , 'Day two and I still lobve my diary')
    entry_three = DiaryEntry('Day 3', 'Okay im still here' )
    my_diary.add(entry_one)
    my_diary.add(entry_two)
    my_diary.add(entry_three)
    assert my_diary.bitsize_section(5, 1) == entry_three


"""
Given a todolist
add 3 tasks
1 task complete
return incomplete list 
"""
my_todo_list = TodoList()
workout = Todo('Workout')
yoga = Todo('Yoga')
run = Todo('Run')
yoga.mark_complete()
my_todo_list.incomplete() # => [workout, run]


"""
Given a todolist
add 3 tasks
1 task complete
return complete list 
"""
def test_complete_list():
    my_todo_list = TodoList()
    workout = Todo('Workout')
    yoga = Todo('Yoga')
    run = Todo('Run')
    my_todo_list.add(workout)
    my_todo_list.add(yoga)
    my_todo_list.add(run)
    yoga.mark_complete()
    assert my_todo_list.complete() == [yoga]



