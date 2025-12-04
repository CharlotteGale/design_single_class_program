from lib.todo_list import *
import pytest

def tests_empty_list_created_on_init():
    """
    On initialisation
    Ensure empty list is created
    """
    todo_list = TodoList()
    assert todo_list.todo_tasks == []


def tests_tasks_added_to_todo_tasks_list():
    """
    Given a task to add_task
    Ensure task is added to self.todo_tasks
    """
    todo_list = TodoList()
    todo_list.add_task("Walk the dog")
    assert todo_list.todo_tasks == ["Walk the dog"]
    todo_list.add_task("Feed the cat")
    assert todo_list.todo_tasks == ["Walk the dog", "Feed the cat"]
    

def tests_returns_list_of_tasks():
    """
    Given read_tasks
    Returns a list of tasks
    """
    todo_list = TodoList()
    todo_list.add_task("Walk the dog")
    todo_list.add_task("Feed the cat")
    assert todo_list.read_tasks() == ["Walk the dog", "Feed the cat"]


def tests_gives_warning_with_empty_string():
    """
    Given an empty string to add_tasks
    Return a warning message that it needs to be a task
    """
    todo_list = TodoList()
    assert todo_list.add_task("") == "Please input a task"


def tests_raises_type_error():
    """
    Given a parameter that is not a string
    Raise a TypeError
    """
    todo_list = TodoList()
    with pytest.raises(TypeError) as e:
        todo_list.add_task(1234)
    error_message = str(e.value)
    assert error_message == "Please input a valid string"