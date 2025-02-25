import pytest

from project import *


def test_check_user_choice():
    assert check_user_choice("1") == True
    with pytest.raises(ValueError):
        assert check_user_choice("abc")
        assert check_user_choice("8")


TASK_FILE = ''


def test_file_not_found():
    assert load_task_list() == []


task_list = []



task_list = [
    {"Description": "Task1", "No": "1", "Status": "Not Done",
     },
]


def test_search_task():
    assert search_task("1", task_list) == [
        {"Description": "Task1", "No": "1", "Status": "Not Done",
         },
    ]
    assert search_task("a", task_list) == []
    assert search_task("2", task_list) == []


def test_get_max_index():
    assert get_max_index(task_list) == 2


def test_back_to_menu():
    assert back_to_menu("b") == print_menu()
    assert back_to_menu("1") is None
    assert back_to_menu("BAck") is None
