from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import User, Project, Task, Comment, Permission, init_db

DATABASE_URI = 'sqlite:///shared_tenant.db'  # Change as needed

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def add_user(tenant_id, username, email, password):
    user = User(tenant_id=tenant_id, username=username, email=email, password=password)
    session.add(user)
    session.commit()
    return user

def add_project(tenant_id, user_id, project_name):
    project = Project(tenant_id=tenant_id, user_id=user_id, project_name=project_name)
    session.add(project)
    session.commit()
    return project

def add_task(tenant_id, project_id, task_name, status):
    task = Task(tenant_id=tenant_id, project_id=project_id, task_name=task_name, status=status)
    session.add(task)
    session.commit()
    return task

def add_comment(tenant_id, task_id, comment_text):
    comment = Comment(tenant_id=tenant_id, task_id=task_id, comment_text=comment_text)
    session.add(comment)
    session.commit()
    return comment

def add_permission(tenant_id, user_id, permission_type):
    permission = Permission(tenant_id=tenant_id, user_id=user_id, permission_type=permission_type)
    session.add(permission)
    session.commit()
    return permission

# Initialize database
init_db(engine)

