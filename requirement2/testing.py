
import unittest
from app import add_task, get_tasks, tasks

class TestApp(unittest.TestCase):
    def test_add_task(self):
        add_task('study swe')
        self.assertIn('study swe', tasks)

    def test_get_tasks(self):
        add_task('Make deep learning bonus')
        self.assertEqual(get_tasks(), ['study swe','Make deep learning bonus'])

if __name__ == '__main__':
    unittest.main()