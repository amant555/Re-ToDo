import os
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from ToDoList import ToDoList
from formatter_todo import console_format

path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
save_file = path + "/MyTasks.txt"


class ToDoListTest(unittest.TestCase):
    # Add Task tests
    @patch('builtins.input', side_effect=["\n\n\n", "\n\n\n"])
    def test_adding_empty_task(self, mock_input):
        todo = ToDoList(console_format)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.add_task()
        self.assertEqual("Empty Task\n", fake_output.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "\n\n\n"])
    def test_adding_body_as_empty_in_task(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        self.assertEqual(["Meet Ema at 7"], todo.incomplete_tasks)

    @patch('builtins.input', side_effect=["\n\n\n", "Meet Ema at 7"])
    def test_adding_head_as_empty_in_task(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        self.assertEqual(["Meet Ema at 7"], todo.incomplete_tasks)

    @patch('builtins.input', side_effect=["Meet Ema at 7", "complete the assignment with her"])
    def test_adding_single_task_in_todo(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        self.assertEqual(["Meet Ema at 7\ncomplete the assignment with her"], todo.incomplete_tasks)

    @patch('builtins.input', side_effect=["Meet Ema at 7", "complete the assignment with her", "Set appointment", "\n"])
    def test_adding_two_tasks_in_todo(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        todo.add_task()
        self.assertEqual(["Meet Ema at 7\ncomplete the assignment with her", "Set appointment"], todo.incomplete_tasks)

    # View Task tests

    def test_viewing_empty_task(self):
        todo = ToDoList(console_format)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.view_and_save_tasks(sys.stdout)
        self.assertEqual("Your TODO list is empty!", fake_output.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "\n\n\n"])
    def test_viewing_task(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.view_and_save_tasks(sys.stdout)
        self.assertEqual("Incomplete Tasks:\n1. Meet Ema at 7\n", fake_output.getvalue())

    # Save Task To a file

    @patch('builtins.input', side_effect=["Meet Ema at 7", "\n\n\n"])
    def test_when_saving_tasks_in_a_file(self, mock_input):
        path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        file_path = path + "/MyTasks.txt"
        todo = ToDoList(console_format)
        todo.add_task()
        todo.view_and_save_tasks(save_file)
        with open(file_path, "r") as file:
            content = file.readlines()
        all_tasks = ''.join([str(elem) for elem in content])
        self.assertEqual("Incomplete Tasks:\n1. Meet Ema at 7\n", all_tasks)
        os.remove(file_path)

    # Mark a task as complete

    @patch('builtins.input', side_effect=["Have Lunch at 1:00pm", "\n", "Meet Ema at 7:00", "\n", 2])
    def test_marking_a_task_as_complete_moves_it_to_the_complete_list(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        todo.add_task()
        todo.mark_completed()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_and_save_tasks(sys.stdout)
            self.assertEqual("Incomplete Tasks:\n1. Have Lunch at 1:00pm\nComplete Tasks:\n1. Meet Ema at 7:00\n",
                             fake_out.getvalue())

    @patch('builtins.input',
           side_effect=["Have Lunch at 1:00pm", "\n", "Meet Ema at 7:00", "\n", "Do your assignments", "\n", "Sleep",
                        "\n", 7])
    def test_the_task_which_is_not_in_list_can_not_be_marked_as_completed(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual(
                "Incomplete Tasks:\n1. Have Lunch at 1:00pm\n2. Meet Ema at 7:00\n3. Do your assignments\n4. "
                "Sleep\n\nThe task you're trying to mark is not present in the list",
                fake_out.getvalue())

    @patch('builtins.input',
           side_effect=["Have Lunch at 1:00pm", "\n", "Meet Ema at 7:00", "\n", "Do your assignments", "\n", "Sleep",
                        "\n", -1])
    def test_when_the_task_number_is_negative_it_can_not_be_marked_as_completed(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.add_task()

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
