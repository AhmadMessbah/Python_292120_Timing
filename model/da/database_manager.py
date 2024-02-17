from sqlalchemy import create_engine,and_, or_
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

from model.entity.base import Base


class DatabaseManager:
    def __init__(self):
        self.session = None
        self.engine = None

    def make_engine(self):
        # mysql+pymysql://user:password@localhost:3306/database_name
        if not database_exists("mysql+pymysql://root:root123@localhost:3306/mft"):
            create_database("mysql+pymysql://root:root123@localhost:3306/mft")

        self.engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")

        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    # def make_engine(self):
    #     if not database_exists("mysql+pymysql://root:root123@localhost:3306/mft"):
    #         create_database("mysql+pymysql://root:root123@localhost:3306/mft")
    #     if not self.engine:
    #         self.engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")
    #         Base.metadata.create_all(self.engine)
    #         self.session_factory = sessionmaker(bind=self.engine)
    #     if not self.session:
    #         self.session = scoped_session(self.session_factory)

    def save(self, entity):
        self.make_engine()
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def edit(self, entity):
        self.make_engine()
        self.session.merge(entity)
        self.session.commit()
        # self.session.refresh(entity)
        self.session.close()
        return entity

    def remove(self, entity):
        self.make_engine()
        self.session.delete(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def remove_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            self.session.refresh(entity)
            self.session.close()
            return entity

    def find_all(self, class_name):
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        self.session.close()
        return entity_list

    def find_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        # self.session.refresh(entity)
        self.session.close()
        return entity

    def find_by_title(self, class_name, title):
        self.make_engine()
        entity = self.session.query(class_name).filter(class_name.title == title).all()
        return entity



