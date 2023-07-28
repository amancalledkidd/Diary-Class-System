
class TodoList():
    def __init__(self):
        self.complete_list = []
        self.incomplete_list = []


    def add(self, todo):
        self.incomplete_list.append(todo)

    def incomplete(self):
        return self.incomplete_list

    def complete(self):
        for todo in self.incomplete_list:
            if todo.completed == True:
                if todo not in self.complete_list:
                    self.incomplete_list.remove(todo)
                    self.complete_list.append(todo)
        return self.complete_list


