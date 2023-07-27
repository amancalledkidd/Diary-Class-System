from lib.diary_entry import *
"""
Check DiaryEntry stores title and contents
"""

first_entry = DiaryEntry("Hi", "Welcome")
assert first_entry.format() == 'Hi: Welcome'

"""
add entry
Check word count
return count
"""

# first_entry = DiaryEntry("Hi", "Welcome")
# first_entry.word_count() # => 1

"""
create entry with phone num
search for phone num
check if correct list is returned
"""
# first_entry = DiaryEntry("Hi", "07949846018")
# first_entry.phone_num_search() # => ["07949846018"]