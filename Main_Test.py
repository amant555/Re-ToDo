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
    

    0. Exit
    1. Add task
    2. View task
    
Incomplete Tasks:
1. Complete the assignment

    0. Exit
    1. Add task
    2. View task
    
'''
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
        self.assertEqual(expected_output, fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
