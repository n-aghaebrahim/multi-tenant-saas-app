import os
import sqlite3
import unittest
from scripts.create_shared_database import create_shared_database

class TestCreateSharedDatabase(unittest.TestCase):

    def setUp(self):
        create_shared_database()

    def tearDown(self):
        os.remove('shared_tenant.db')

    def test_database_creation(self):
        connection = sqlite3.connect('shared_tenant.db')
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users';")
        self.assertIsNotNone(cursor.fetchone())

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Projects';")
        self.assertIsNotNone(cursor.fetchone())

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Tasks';")
        self.assertIsNotNone(cursor.fetchone())

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Comments';")
        self.assertIsNotNone(cursor.fetchone())

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Permissions';")
        self.assertIsNotNone(cursor.fetchone())

        connection.close()

if __name__ == '__main__':
    unittest.main()

