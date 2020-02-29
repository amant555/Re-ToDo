import os
import unittest
from io import StringIO
from Main import main
from unittest.mock import patch


class Main_Test(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, "Complete the assignment", "\n", 2, 0])
    def testing_console_for_one_task_and_viewing_it(self, mock_input):
        expected_output = '''
    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    

    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    
Incomplete Tasks:
1. Complete the assignment

    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    
'''
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
        self.assertEqual(expected_output, fake_out.getvalue())

    @patch('builtins.input', side_effect=[1, "Complete the assignment", "\n", 1, "Meet Ema at 7", "\n", 3, 1, 2, 0])
    def testing_console_for_two_task_and_marking_one_as_complete_then_viewing_it(self, mock_input):
        expected_output = '''
    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    

    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    

    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    
Incomplete Tasks:
1. Complete the assignment
2. Meet Ema at 7

    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    
Incomplete Tasks:
1. Meet Ema at 7
Complete Tasks:
1. Complete the assignment

    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    
'''
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
        self.assertEqual(expected_output, fake_out.getvalue())

    @patch('builtins.input', side_effect=[1, "Complete the assignment", "\n", 1, "Meet Ema at 7", "\n", 3, 1, 2, 4, 0])
    def testing_console_for_two_task_and_marking_one_as_complete_then_saving_it_to_file(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
        path_desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        file_path = path_desktop + "/MyTasks.txt"
        with open(file_path, "r") as file:
            content = file.readlines()
        all_tasks = ''.join([str(elem) for elem in content])
        self.assertEqual("Incomplete Tasks:\n1. Meet Ema at 7\nComplete Tasks:\n1. Complete the assignment\n",
                         all_tasks)
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
