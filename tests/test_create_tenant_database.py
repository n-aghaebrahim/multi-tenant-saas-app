import os
import sqlite3
import unittest
from scripts.create_tenant_database import create_tenant_database

class TestCreateTenantDatabase(unittest.TestCase):

    def setUp(self):
        self.tenant_id = 1
        create_tenant_database(self.tenant_id)

    def tearDown(self):
        os.remove(f'{self.tenant_id}.db')

    def test_database_creation(self):
        connection = sqlite3.connect(f'{self.tenant_id}.db')
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

