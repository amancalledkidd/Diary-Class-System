class Diary():
#     # User facing props:
#         # List of diary entry instances
#         # list of from phone numbers from diary entries
#         # Perhaps some way of listing todos?????
    

    def __init__(self):
        self.diary_entries = []
        self.phone_nums = []
        self.todos = []

    def list_entries(self):
        return self.diary_entries

#     def add(self, entry):
#         # parameter:
#             # variable: instance of diary entry class
#         # Returns:
#             # nothing
#         # side_effect:
#             # adds to self diary entry list
#         pass

#     def get_phone_nums(self):
#         # returns:
#             # list of phone nums
#         # side effect:
#             # gets nums from current diary entries
        
#         # could add if statement to check if num already exists? Later development perhaps?
#         pass

#     def bitsize_section(self, wpm, minutes):
#         # Parameters
#         #   wpm: a int representing words per minute
#         #   minutes: integer
#         # Returns 
#         #   a readble entry
#         pass

#     def get_todo(self):
#         # Checks for todos in diary entry
#         # todo exists
#         # create todo
#         # add to todolist
#         # returns list of incomplete todos
#         pass