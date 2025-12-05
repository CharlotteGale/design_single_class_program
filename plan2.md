# TODO Class Plan

## 1. Describe the Problem
> As a user     
> So that I can focus on tasks to complete      
> I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface
```python
class TodoList():
    def __init__(self):
        # Parameters:
        #   None
        # Side Effects:
        #   None
        # Internal State:
        #   Initializes an empty list to track tasks
        #       self.todo_tasks = []
        pass

    def add_task(self, task, is_complete=False):
        # Parameters:
        #   task: string
        #   is_complete: boolean (defaulted to False)
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

    def mark_task_complete(self, task):
        # Paramenters:
        #   task: string
        # Returns:
        #   Nothing
        # Side effects:
        #   Saves the task property to the self object as complete
```

## 3. Create Examples as Tests
```python
"""
When given a `task` is passed into `mark_task_complete`
Marks `is_complete` as True to associated task
"""
todo_list = TodoList()
todo_list.add_task("Have a nap")
todo_list.add_task("Go for a walk")
todo_list.mark_task_complete("Have a nap")

assert todo_list.todo_tasks == [["Have a nap", True], ["Go for a walk", False]]
```

## 4. Implement the Behaviour
Building on the logic from the first user story under `plan1.md` 
I will continue to use `self.todo_tasks` list but make it a nested list.
`add_task` will have an additional default parameter of `False`.