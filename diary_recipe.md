# Diary Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries


As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

* Main class diary
* Secondary class diary entry - may need option for mobile phone numbers in this class
* Secondary class todo list which will need a todo class to support


## 2. Design the Class System

```

 ┌─────────────────────┐     ┌─────────────────────┐
 │Diary Class          │     │TodoList Class       │
 │                     │     │                     │
 │ -store entries      │     │ -Store incomplete   │
 │                     │     │ -store complet      │
 │ -read in sections  ─┼─────┼─►                   │
 │                     │     │ -count lists        │
 │ -show todos        ◄├─────┼──                   │
 │                     │     │                     │
 │ -Phone number list  │     │                     │
 │         │           │     │          │          │
 └─────────┼───────────┘     └──────────┼──────────┘
           │                            │
           │                            │
           ▼                            ▼
 ┌─────────────────────┐     ┌─────────────────────┐
 │DiaryEntry Class     │     │Todo class           │
 │                     │     │                     │
 │ - Title             │     │ -create Todos       │
 │ - contents          │     │ -Mark todos complete│
 │ -Phone number list  │     │                     │
 │                     │     │                     │
 │                     │     │                     │
 │                     │     │                     │
 │                     │     │                     │
 │                     │     │                     │
 └─────────────────────┘     └─────────────────────┘



```

_Also design the interface of each class in more detail._

```python

# lib/Diary.py

class Diary():
    # User facing props:
        # List of diary entry instances
        # list of from phone numbers from diary entries
        # Perhaps some way of listing todos?????
    

    def __init__(self):
        # self.diary_entries = []
        # self.phone_nums = []
        # self.todos = []
        pass

    def list_entries(self):
        # Returns list of entries

    def add(self, entry):
        # parameter:
            # variable: instance of diary entry class
        # Returns:
            # nothing
        # side_effect:
            # adds to self diary entry list
        pass

    def get_phone_nums(self):
        # returns:
            # list of phone nums
        # side effect:
            # gets nums from current diary entries
        
        # could add if statement to check if num already exists? Later development perhaps?
        pass

    def bitsize_section(self, wpm, minutes):
        # Parameters
        #   wpm: a int representing words per minute
        #   minutes: integer
        # Returns 
        #   a readble entry

    def get_todo(self):
        # Checks for todos in diary entry
        # todo exists
        # create todo
        # add to todolist
        # returns list of incomplete todos
        pass

# lib/diary_entry.py

class DiaryEntry():
    # User facing properties:
        # a list to store any phone numbers in content
        # a list to store todos
    
    
    def __init__(self, title, contents):
        # Parameters:
            # ttile: string of words to name the entry
            # contents: string of words for the entry
        pass

    def format(self):
        # Return string of title and contents combined


    def word_count(self):
        # returns:
            #  word count as integer by spliting contents
        pass
    def phone_num_search(self):
        # searches entry contents for phone numbers 
        # stores the numbers in list
        # Returns:
        #   phone number list 
        pass

    def todo_search(self):
        # searchs for Todos in content 
        # If todo exists
        # add to todolist

# lib/todo_list.py

class TodoList():
    #User facing properties:
    #   Stores Todos in list
    #  secondlist for complete todos
    # Extra stuff.... dictionnary to store todos completetion times?  accesible by diary maybe?
    def __init__(self):
        pass

    def add(self, todo):
        # parameter: 
        #   todo: instance of todo class
        # returns:
        #   nothing
        pass

    def incomplete(self):
        # returns:
        # A list of completed tasks
        pass

    def complete(self):
        # Returns: list of completed tasks
        pass

    def count_complete(self):
        # returns: number of completed tasks
        pass

# lib/todo.py

class Todo():
    # Properties:
    #  stores task
    #  stores if task is complete
    
    def __init__(self, task):
        # parameter:
            # task: string of words repesenting a task
        pass

    def mark_complete(self):
        # side effect:
        #  Marks task complete
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python


"""
Given a diary
When we add two entries
We see those entries reflected in the entries list
"""

my_diary = Diary()
entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, exciting times')
entry_two = DiaryEnrty('Round 2' , 'Day two and I still lobve my diary')
my_diary.add(entry_one)
my_diary.add(entry_two)
my_diary.list_entries() # => [entry_one, entry_two]

"""
Given a diary
when two entries are added
when both entries have phone numbers
return a list of those phone numbers
"""
my_diary = Diary()
entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, my number is 07946464535 exciting times')
entry_two = DiaryEnrty('Round 2' , 'Day two and I still lobve my diary 07956289016')
my_diary.add(entry_one)
my_diary.add(entry_two)
entry_one.phone_num_search()
entry_two.phone_num_search()
my_diary.get_phone_nums() # => ['07946464535', '07956289016']

"""
Given diary
When two entries are added with todos
return list of incomplete todos
"""

my_diary = Diary()
my_todo_list = TodoList()
entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, #TODO Get phone numbers')
entry_two = DiaryEnrty('Round 2' , 'Day two and I still lobve my diary #TODO Do some shopping')
workout = todo('Workout')
my_todo_list.add(workout)
my_diary.add(entry_one)
my_diary.add(entry_two)
entry_one.todo_search()
entry_two.todo_search()
my_diary.get_todo() # => [workout, Get phone numbers, Do some shopping

"""
given a diary
when the diary has three entries
returns a entry that will be readble within given time and read_speed
"""

my_diary = Diary()
entry_one = DiaryEntry('Hello, World', 'Welcome to my diary, exciting times')
entry_two = DiaryEntry('Round 2' , 'Day two and I still lobve my diary')
entry_three = DiaryEntry('Day 3', 'Okay im still here' )
my_diary.add(entry_one)
my_diary.add(entry_two)
my_diary.bitsize_section(5, 1) # => entry_three


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
my_todo_list = TodoList()
workout = Todo('Workout')
yoga = Todo('Yoga')
run = Todo('Run')
yoga.mark_complete()
my_todo_list.incomplete() # => [yoga]


"""
Given a todolist
add 3 tasks
2 task complete
return complete count 
"""
my_todo_list = TodoList()
workout = Todo('Workout')
yoga = Todo('Yoga')
run = Todo('Run')
yoga.mark_complete()
workout.mark_complete()
my_todo_list.count_complete() # =>2



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

"""
Check todo intialises task
"""

workout = Todo('Workout')
workout.task # => 'Workout'

"""
Check mark complete updates self object
"""
workout = Todo('Workout')
workout.mark_complete()
workout.complete # => True

"""
Check DiaryEntry stores title and contents
"""

first_entry = DiaryEntry("Hi", "Welcome")
first_entry.format # => 'Hi: Welcome

"""
add entry
Check word count
return count
"""

first_entry = DiaryEntry("Hi", "Welcome")
first_entry.word_count() # => 1

"""
create entry with phone num
search for phone num
check if correct list is returned
"""
first_entry = DiaryEntry("Hi", "07949846018")
first_entry.phone_num_search() # => ["07949846018"]

"""
Create entry with todo
call todo search
return todo list
"""
first_entry = DiaryEntry("Hi", "#TODO Go for run")
first_entry.todo_search() # => [Go for run]

"""
create diary
return empty list of entries
"""

my_diary = Diary()
my_diary.list_entries() # => []

"""
create todo list instance
check check todo List initalises
"""
todo_list = TodoList()
todo_list.incomplete_list # => []

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
