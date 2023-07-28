class DiaryEntry():

    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents
        self.phone_numbers = []
        self._todo_list = []


    def format(self):
        return f"{self.title}: {self.contents}"


    def word_count(self):
        return len(self.contents.split())


    def phone_num_search(self):
        word_list = self.contents.split()
        for word in word_list:
            if len(word) == 11 and word.isnumeric():
                if word not in self.phone_numbers:
                    self.phone_numbers.append(word)
        return self.phone_numbers
