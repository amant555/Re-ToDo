import unittest
from io import StringIO
from unittest.mock import patch
from ToDoList import ToDoList


class ToDoListTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["\n\n\n", "\n\n\n"])
    def test_adding_empty_task(self, mock_input):
        todo = ToDoList()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            todo.add_task()
        self.assertEqual("Empty Task\n", fake_output.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "\n\n\n"])
    def test_adding_body_as_empty_in_task(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        self.assertEqual(["Meet Ema at 7"], todo.incomplete_tasks)

    @patch('builtins.input', side_effect=["\n\n\n", "Meet Ema at 7"])
    def test_adding_head_as_empty_in_task(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        self.assertEqual(["Meet Ema at 7"], todo.incomplete_tasks)

    @patch('builtins.input', side_effect=["Meet Ema at 7", "complete the assignment with her"])
    def test_adding_single_task_in_todo(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        self.assertEqual(["Meet Ema at 7\ncomplete the assignment with her"], todo.incomplete_tasks)

    @patch('builtins.input', side_effect=["Meet Ema at 7", "complete the assignment with her", "Set appointment", "\n"])
    def test_adding_two_tasks_in_todo(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        todo.add_task()
        self.assertEqual(["Meet Ema at 7\ncomplete the assignment with her", "Set appointment"], todo.incomplete_tasks)


if __name__ == '__main__':
    unittest.main()
