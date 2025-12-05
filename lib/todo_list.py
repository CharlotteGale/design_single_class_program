class TodoList():
    def __init__(self):
        self.todo_tasks = []

    def add_task(self, task, is_complete=False):
        if not isinstance(task, str):
            raise TypeError("Please input a valid string")
        
        if task == "":
            return "Please input a task"
        
        self.todo_tasks.append([task, is_complete])

    def mark_task_complete(self, task):
        for todo in self.todo_tasks:
            if todo[0] == task:
                todo[1] = True

    def read_tasks(self):
        incomplete_tasks = []

        for todo in self.todo_tasks:
            if todo[1] == False:
                incomplete_tasks.append(todo[0])

        return incomplete_tasks