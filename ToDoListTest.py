import os
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from ToDoList import ToDoList
from Formatter_ToDo import console_format

path = "."  # os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
save_file = path + "/MyTasks.txt"


def get_todo_list_with(tasks):
    todo = ToDoList(console_format)
    for task in tasks:
        todo.add_task(task)
    return todo


class AddTaskTest(unittest.TestCase):
    def test_adding_empty_task(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            get_todo_list_with(["\n\n\n"])
        self.assertEqual("Empty Task\n", fake_output.getvalue())

    def test_adding_body_as_empty_in_task(self):
        todo = get_todo_list_with(["Meet Ema at 7" + "\n\n\n"])
        self.assertEqual(["Meet Ema at 7"], todo.incomplete_tasks)

    def test_adding_head_as_empty_in_task(self):
        todo = get_todo_list_with(["\n\n\n" + "Meet Ema at 7"])
        self.assertEqual(["Meet Ema at 7"], todo.incomplete_tasks)

    def test_adding_single_task_in_todo(self):
        todo = get_todo_list_with(["Meet Ema at 7" + "\ncomplete the assignment with her"])
        self.assertEqual(["Meet Ema at 7\ncomplete the assignment with her"], todo.incomplete_tasks)

    def test_adding_two_tasks_in_todo(self):
        todo = get_todo_list_with(["Meet Ema at 7" + "\ncomplete the assignment with her", "Set appointment" + "\n"])
        self.assertEqual(["Meet Ema at 7\ncomplete the assignment with her", "Set appointment"], todo.incomplete_tasks)


class ViewTaskTest(unittest.TestCase):

    def test_viewing_empty_task(self):
        todo = ToDoList(console_format)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.view_and_save_tasks(sys.stdout)
        self.assertEqual("Your TODO list is empty!", fake_output.getvalue())

    def test_viewing_task(self):
        todo = get_todo_list_with(["Meet Ema at 7" + "\n\n\n"])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.view_and_save_tasks(sys.stdout)
        self.assertEqual("Incomplete Tasks:\n1. Meet Ema at 7\n", fake_output.getvalue())


class SaveTaskToFile(unittest.TestCase):
    def test_when_saving_tasks_in_a_file(self):
        todo = get_todo_list_with(["Meet Ema at 7" + "\n\n\n"])
        todo.view_and_save_tasks(save_file)
        with open(save_file, "r") as file:
            content = file.readlines()
        all_tasks = ''.join([str(elem) for elem in content])
        self.assertEqual("Incomplete Tasks:\n1. Meet Ema at 7\n", all_tasks)
        os.remove(save_file)


class MarkTaskAsComplete(unittest.TestCase):
    @patch('builtins.input', side_effect=[2])
    def test_marking_a_task_as_complete_moves_it_to_the_complete_list(self, mock_input):
        todo = get_todo_list_with(["Have Lunch at 1:00pm" + "\n", "Meet Ema at 7:00" + "\n"])
        todo.mark_completed()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_and_save_tasks(sys.stdout)
            self.assertEqual("Incomplete Tasks:\n1. Have Lunch at 1:00pm\nComplete Tasks:\n1. Meet Ema at 7:00\n",
                             fake_out.getvalue())

    @patch('builtins.input', side_effect=[7])
    def test_the_task_which_is_not_in_list_can_not_be_marked_as_completed(self, mock_input):
        todo = get_todo_list_with(["Have Lunch at 1:00pm" + "\n", "Meet Ema at 7:00" + "\n"
                                      , "Do your assignments" + "\n", "Sleep" + "\n"])
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual(
                "Incomplete Tasks:\n1. Have Lunch at 1:00pm\n2. Meet Ema at 7:00\n3. Do your assignments\n4. "
                "Sleep\n\nThe task you're trying to mark is not present in the list",
                fake_out.getvalue())

    @patch('builtins.input', side_effect=[-1])
    def test_when_the_task_number_is_negative_it_can_not_be_marked_as_completed(self, mock_input):
        todo = get_todo_list_with(["Have Lunch at 1:00pm" + "\n", "Meet Ema at 7:00" + "\n"
                                      , "Do your assignments" + "\n", "Sleep" + "\n"])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual(
                "Incomplete Tasks:\n1. Have Lunch at 1:00pm\n2. Meet Ema at 7:00"
                "\n3. Do your assignments\n4. Sleep\n\nThe task you're trying to mark is not present in the list",
                fake_out.getvalue())

    def test_when_TODO_list_is_empty_then_to_mark_a_task_as_complete_is_not_allowed(self):
        todo = ToDoList(console_format)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual("\nYour TODO list is empty!", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
