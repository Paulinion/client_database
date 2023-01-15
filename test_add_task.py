import unittest
import main
import time
import pandas as pd

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.system = main.ContactControl()
        self.system.add_user('1', 'Dmitry', 0)
        self.system.add_user('2', 'Alexandr', 1)
        self.system.add_task('Nastya', 'Dmitry', 'send fax', time.strftime("%H:%M:%S", time.localtime()), 1)
        self.system.add_task('Nastya', 'Alexandr', 'send email', time.strftime("%H:%M:%S", time.localtime()), 1)
        self.system.add_client('DSX', 'asd2@gmail.com', 'Nastya')
        # self.system.

    # Проверка на ошибку при неверном количестве аргументов
    def test_add_task(self):
        self.assertRaises(TypeError, lambda: self.system.add_task('Nastya'))


if __name__ == '__main__':
    unittest.main()
