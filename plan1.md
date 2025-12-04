# TODO Class Plan

## 1. Describe the Problem
> As a user     
> So that I can keep track of my tasks      
> I want a program that I can add todo tasks to and see a list of them.

## 2. Design the Class Interface
```python
class TodoList():
    def __init__(self):
        # Parameters:
        #   None
        # Side Effects:
        #   None
        # State:
        #   Initializes an empty list to track tasks
        #       self.todo_tasks = []
        pass

    def add_task(self, task):
        # Parameters:
        #   task: string
        # Returns:
        #   Nothing
        # Side Effects:
        #   Saves the task property to the self object
        pass
    
    def read_tasks(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of tasks
        pass

```

## 3. Create Examples as Tests
```python
"""
On initialisation
Ensure empty list is created
"""
todo_list = TodoList()
assert todo_list.todo_tasks == []
```
```python
"""
Given a task to add_task
Ensure task is added to self.todo_tasks
"""
todo_list = TodoList()
todo_list.add_task("Walk the dog")
assert todo_list.todo_tasks == ["Walk the dog"]
todo_list.add_task("Feed the cat")
assert todo_list.todo_tasks == ["Walk the dog", "Feed the cat"]
```
```python
"""
Given read_tasks
Returns a list of tasks
"""
todo_list = TodoList()
todo_list.add_task("Walk the dog")
todo_list.add_task("Feed the cat")
assert todo_list.read_tasks() == ["Walk the dog", "Feed the cat"]
```
```python
"""
Given an empty string to add_tasks
Return a warning message that it needs to be a task
"""
todo_list = TodoList()
assert todo_list.add_task("") == "Please input a task"
```
```python
"""
Given a parameter that is not a string
Raise a TypeError
"""
todo_list = TodoList()
with pytest.raises(TypeError) as e:
    todo_list.add_task(1234)
error_message = str(e.value)
assert error_message == "Please input a valid string"
```
