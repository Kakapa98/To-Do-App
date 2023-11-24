import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from to_do_list import add_task, mark_done, view_tasks, load_tasks, save_tasks, tasks, main_menu


class TestTodoListFunctions(unittest.TestCase):
    def setUp(self):
        tasks.clear()  # Clear tasks before each test

    def test_load_tasks_positive(self):
        # Positive Test: File exists
        with patch("builtins.open", mock_open(read_data='[{"task": "Task 1", "done": false}]')):
            result = load_tasks()
        self.assertEqual(result, [{"task": "Task 1", "done": False}])

    def test_load_tasks_negative(self):
        # Negative Test: File not found
        with patch("builtins.open", side_effect=FileNotFoundError()):
            result = load_tasks()
        self.assertEqual(result, [])

    def test_save_tasks(self):
        # Positive Test
        tasks.extend([
            {"task": "Task 1", "done": False},
            {"task": "Task 2", "done": True},
        ])

        with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
            save_tasks()

        mock_json_dump.assert_called_once_with(tasks, mock_file.return_value)

    def test_add_task_positive(self):
        # Positive Test
        with patch("builtins.input", side_effect=["New Task"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            add_task()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], "New Task")
        self.assertFalse(tasks[0]['done'])

        expected_output = "Task added!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_add_task_negative(self):
        # Negative Test: Invalid task name (empty input)
        with patch("builtins.input", side_effect=[""]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            add_task()

        self.assertEqual(len(tasks), 0)  # No new task should be added
        self.assertEqual(mock_stdout.getvalue(), "Invalid task name. Task not added.\n")

    def test_mark_done_positive(self):
        # Positive Test
        tasks.append({"task": "Test Task", "done": False})
        with patch("builtins.input", side_effect=["1"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            mark_done()

        self.assertTrue(tasks[0]['done'])

        expected_output = "Tasks:\n1. Test Task - Not Done\nTask marked as done!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_mark_done_negative_invalid_number(self):
        # Negative Test: Invalid task number
        with patch("builtins.input", side_effect=["0"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            mark_done()

        if tasks:
            self.assertFalse(tasks[0]['done'])  # The task should remain unchanged
        else:
            self.assertEqual(mock_stdout.getvalue(), "Tasks:\nInvalid task number.\n")

    def test_mark_done_negative_invalid_input(self):
        # Negative Test: Invalid input (non-integer)
        with patch("builtins.input", side_effect=["0"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            mark_done()

        # Check if tasks list is empty before attempting to access the first element
        if tasks:
            self.assertFalse(tasks[0]['done'])  # The task should remain unchanged
        else:
            self.assertEqual(mock_stdout.getvalue(), "Tasks:\nInvalid task number.\n")

    def test_view_tasks(self):
        # Positive Test
        tasks.extend([
            {"task": "Task 1", "done": False},
            {"task": "Task 2", "done": True},
            {"task": "Task 3", "done": False},
        ])
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            view_tasks()

        expected_output = "Tasks:\n1. Task 1 - Not Done\n2. Task 2 - Done\n3. Task 3 - Not Done\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_main_menu_exit(self):
        # Positive Test
        with patch("builtins.input", return_value="4"), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main_menu()

        expected_output = "\n1. Add Task\n2. Mark Task as Done\n3. View Tasks\n4. Exit\nTasks saved. Goodbye!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_save_tasks_positive(self):
        # Positive Test: Save tasks to file
        tasks.extend([
            {"task": "Task 1", "done": False},
            {"task": "Task 2", "done": True},
            {"task": "Task 3", "done": False},
        ])

        with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
            save_tasks()

        mock_json_dump.assert_called_once_with(tasks, mock_file.return_value)

    def test_load_tasks_positive(self):
        # Positive Test: Load tasks from file
        tasks.clear()
        with patch("builtins.open", mock_open(read_data='[{"task": "Task 1", "done": false}]')) as mock_file:
            load_tasks()

        self.assertEqual(len(tasks), 0)
        

    def test_load_tasks_negative_file_not_found(self):
        # Negative Test: FileNotFoundError during loading
        with patch("builtins.open", side_effect=FileNotFoundError()), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            load_tasks()

        self.assertEqual(len(tasks), 0)
        self.assertEqual(mock_stdout.getvalue(), "")

if __name__ == "__main__":
    unittest.main()

