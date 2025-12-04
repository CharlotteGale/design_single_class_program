class TodoList():
    def __init__(self):
        self.todo_tasks = []

    def add_task(self, task):
        if not isinstance(task, str):
            raise TypeError("Please input a valid string")
        
        if task == "":
            return "Please input a task"
        
        self.todo_tasks.append(task)

    def read_tasks(self):
        return self.todo_tasks