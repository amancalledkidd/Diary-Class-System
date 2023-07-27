class DiaryEntry():
    # User facing properties:
        # a list to store any phone numbers in content
        # a list to store todos

    
    
    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents
        self.phone_numbers = []
        self._todo_list = []

    def format(self):
        return f"{self.title}: {self.contents}"


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
        pass