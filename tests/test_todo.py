from lib.todo import Todo

"""
Check todo intialises task
"""
def test_check_task():
    workout = Todo('Workout')
    assert workout.task == 'Workout'

"""
Check mark complete updates self object
"""
def test_mark_complete():
    workout = Todo('Workout')
    workout.mark_complete()
    assert workout.completed == True