import unittest
from src.queries import add_user, add_project, add_task, add_comment, add_permission, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class TestQueries(unittest.TestCase):

    def setUp(self):
        self.tenant_id = 1

    def test_add_user(self):
        user = add_user(self.tenant_id, 'testuser', 'test@example.com', 'password')
        self.assertIsNotNone(user.user_id)

    def test_add_project(self):
        user = add_user(self.tenant_id, 'testuser', 'test@example.com', 'password')
        project = add_project(self.tenant_id, user.user_id, 'Test Project')
        self.assertIsNotNone(project.project_id)

    def test_add_task(self):
        user = add_user(self.tenant_id, 'testuser', 'test@example.com', 'password')
        project = add_project(self.tenant_id, user.user_id, 'Test Project')
        task = add_task(self.tenant_id, project.project_id, 'Test Task', 'Pending')
        self.assertIsNotNone(task.task_id)

    def test_add_comment(self):
        user = add_user(self.tenant_id, 'testuser', 'test@example.com', 'password')
        project = add_project(self.tenant_id, user.user_id, 'Test Project')
        task = add_task(self.tenant_id, project.project_id, 'Test Task', 'Pending')
        comment = add_comment(self.tenant_id, task.task_id, 'This is a comment')
        self.assertIsNotNone(comment.comment_id)

    def test_add_permission(self):
        user = add_user(self.tenant_id, 'testuser', 'test@example.com', 'password')
        permission = add_permission(self.tenant_id, user.user_id, 'read')
        self.assertIsNotNone(permission.permission_id)

if __name__ == '__main__':
    unittest.main()

