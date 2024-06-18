from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class Project(Base):
    __tablename__ = 'Projects'
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    project_name = Column(String, nullable=False, unique=True)
    user = relationship('User')

class Task(Base):
    __tablename__ = 'Tasks'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    project_id = Column(Integer, ForeignKey('Projects.project_id'), nullable=False)
    task_name = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)
    project = relationship('Project')

class Comment(Base):
    __tablename__ = 'Comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    task_id = Column(Integer, ForeignKey('Tasks.task_id'), nullable=False)
    comment_text = Column(Text, nullable=False)
    task = relationship('Task')

class Permission(Base):
    __tablename__ = 'Permissions'
    permission_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    permission_type = Column(String, nullable=False)
    user = relationship('User')

def init_db(engine):
    Base.metadata.create_all(engine)

