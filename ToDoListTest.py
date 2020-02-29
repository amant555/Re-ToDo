import unittest
from io import StringIO
from unittest.mock import patch
from ToDoList import ToDoList
from formatter_todo import console_format


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
            todo.view_tasks()
        self.assertEqual("Your TODO list is empty!", fake_output.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "\n\n\n"])
    def test_viewing_task(self, mock_input):
        todo = ToDoList(console_format)
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.view_tasks()
        self.assertEqual("Incomplete Tasks:\n1. Meet Ema at 7", fake_output.getvalue())


if __name__ == '__main__':
    unittest.main()
