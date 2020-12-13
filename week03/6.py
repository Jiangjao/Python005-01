#!/usr/bin/env python3
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)
# 张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性

import time
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey,collate,decimal
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 连接数据库，
db = pymysql.connect("127.0.0.1",
                     "root", 
                     "password", 
                     "testdb",
                     autocommit=True,    # 如果插入数据，和conn.commit()功能一致。
                     )

#表结构
Base = declarative_base()

class userinfo(Base):
    __tablename__ = 'userinfo'
    uid = Column(Integer(), primary_key=True, nullable=False,autoincrement=True,comment='姓名')
    name = Column(String(15),nullable=False, unique=True, COMMENT='用户信息表')

class usermoney(Base):
    __tablename__ = 'usermoney'
    uid = Column(Integer(), primary_key=True, nullable=False,autoincrement=True,comment='姓名')
    money = Column(String(15),nullable=False, unique=True, COMMENT='用户资产')

class userlog(Base):
    __tablename__ = 'userlog'
    uid = Column(Integer(), primary_key=True, nullable=False,autoincrement=True,comment='姓名')
    out_id = Column(Integer(), nullable=False, unique=True,comment='转出id')
    in_id = Column(Integer(), nullable=False, unique=True,comment='转入id')
    money = Column(String(15),nullable=False, unique=True, COMMENT='操作金额')
    update_time =  Column(DateTime(), nullable=False, unique=True, default=datetime.now,comment='操作时间')

db.commit()


    # collate(uid, 'utf8_bin')
# CREATE TABLE `userinfo` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
#   `name` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '姓名',
#   PRIMARY KEY (`id`),
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='用户信息表';


# CREATE TABLE `usermoney` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户id',
#   `money` decimal(10,2) DEFAULT NULL COMMENT '用户资产',
#   PRIMARY KEY (`id`),
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='用户资产表';

# CREATE TABLE `userlog` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
#   `out_id` int(11) DEFAULT NULL COMMENT '转出id',
#   `in_id` int(11) DEFAULT NULL COMMENT '转入id',
#   `update_time` int(11) DEFAULT NULL COMMENT '操作时间',
#   `money` decimal(10,2) DEFAULT NULL COMMENT '操作金额',
#   PRIMARY KEY (`id`),
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='操作记录表';


class TransferMoney(object):
    # 构造方法
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def transfer(self, source_id, target_id, money):
        # 1). 判断两个账号是否存在?
        # 2). 判断source_id是否有足够的钱？
        # 3). source_id扣钱
        # 4). target_id加钱
        if not self.check_account_avaialbe(source_id):
            raise  Exception("账户不存在")
        if not self.check_account_avaialbe(target_id):
            raise  Exception("账户不存在")

        if self.has_enough_money(source_id, money):
            try:
                self.reduce_money(source_id, money)
                self.add_money(target_id, money)
            except Exception as e:
                print("转账失败:", e)
                self.conn.rollback()
            else:
                self.conn.commit()
                print("%s给%s转账%s金额成功" % (source_id, target_id, money))

    def check_account_avaialbe(self, acc_id):
        """判断帐号是否存在， 传递的参数是卡号的id"""
        select_sqli = "select * from userinfo where id=%d;" % (acc_id)
        print("execute sql:", select_sqli)
        res_count = self.cur.execute(select_sqli)
        if res_count == 1:
            return True
        else:
            # raise  Exception("账户%s不存在" %(acc_id))
            return False

    def has_enough_money(self, acc_id, money):
        """判断acc_id账户上金额> money"""
        # 查找acc_id存储金额?
        select_sqli = "select money from bankData where id=%d;" % (acc_id)
        print("execute sql:", select_sqli)
        self.cur.execute(select_sqli)  # ((1, 500), )

        # 获取查询到的金额钱数;
        acc_money = self.cur.fetchone()[0]
        print("余额为：%d"%acc_money)
        # 判断
        if acc_money >= money:
            return True
        else:
            return False

    def add_money(self, acc_id, money):
        update_sqli = "update bankData set money=money+%d  where id=%d" % (money, acc_id)
        print("add money:", update_sqli)
        self.cur.execute(update_sqli)

    def reduce_money(self, acc_id, money):
        update_sqli = "update bankData set money=money-%d  where id=%d" % (money, acc_id)
        print("reduce money:", update_sqli)
        self.cur.execute(update_sqli)

    # 析构方法
    def __del__(self):
        self.cur.close()
        self.conn.close()

# 模拟转账，执行事务
trans = TransferMoney(db)
assert trans.check_account_avaialbe(14255632) == False
assert  trans.check_account_avaialbe(13997) == True
#
#
assert  trans.has_enough_money(13997, 100) == False
assert  trans.has_enough_money(13998, 100) == True
trans.add_money(13998, 100)
trans.reduce_money(13998, 100)
# trans.transfer(12567, 16787, 100)
trans.transfer(13997, 13998, 200)

db.close()
