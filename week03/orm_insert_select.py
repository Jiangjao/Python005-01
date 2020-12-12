# ORM 方式连接MySQL数据库
# pip3 install sqlalchemy
# !/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 打开数据库连接
# mysql > create database testdb;
# mysql > GRANT ALL PRIVILEGES ON testdb. *TO 'testuser'@'%' IDENTIFIED BY 'testpass';
Base = declarative_base()

class Person_table(Base):
    __tablename__ = 'collection_individual'
    person_id = Column(Integer(), primary_key=True)
    person_name = Column(String(50), index=True)
    person_age = Column(String(50), index=True)
    person_birthday = Column(String(50), index=True)
    person_sex = Column(String(50), index=True)
    person_degree = Column(String(50), index=True)
    field_created_time =  Column(DateTime(), default=datetime.now)
    field_updated_time =  Column(DateTime(), default=datetime.now,onupdate=datetime.now)

    def __repr__(self):
        return "Person_table(person_id='{self.person_id}',"\
            "person_name={self.person_name})".format(self=self)

# Float
# Decimal
# Boolean
# Text
# autoincrement

# 业务逻辑
# 持久层
# 数据库层

# 实例一个引擎
dburl = 'mysql+pymysql://root:Dj224768@localhost:3306/zhihu_te?charset=utf8mb4'
engine = create_engine(dburl, echo=True,encoding='utf-8')
# Base.metadata.create_all(engine)

# 创建一个session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
individual_demo = Person_table(person_id=1,person_name='jack')
individual_demo2 = Person_table(person_name='Mary')
session.add(individual_demo)
session.add(individual_demo2)
session.flush()



# 查询数据
# result = session.query(Person_table).all()
# for result in session.query(Person_table):
#     print(result)

# 排序
# from sqlalchemy import desc
# for result in session.query(Person_table).order_by(desc(Person_table.book_id)).limit(3):
#     print(result)


# print(result)

session.commit()










