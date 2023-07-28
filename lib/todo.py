class Todo():

    def __init__(self, task):
        self.task = task
        self.completed = False

    def mark_complete(self):
        self.completed = True