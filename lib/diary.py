
class Diary():
    

    def __init__(self):
        self.diary_entries = []
        self.phone_nums = []
        self.todos = []

    def list_entries(self):
        return self.diary_entries

    def add(self, entry):
        self.diary_entries.append(entry)

    def get_phone_nums(self):
        for entry in self.diary_entries:
            num_list = entry.phone_num_search()
            if num_list != []:
                print(num_list)
                for nums in num_list:
                    self.phone_nums.append(nums)
        return self.phone_nums

    def bitsize_section(self, wpm, minutes):
        import math
        read_size = wpm * minutes
        best_option_num = 0
        for entry in self.diary_entries:
            if entry.word_count() < read_size:
                if entry.word_count() > best_option_num:
                    best_option = entry
                    best_option_num = entry.word_count()
        return best_option

    def get_todo(self, todo_list):
        return todo_list.incomplete()