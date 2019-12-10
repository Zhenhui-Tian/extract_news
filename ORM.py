# coding=utf-8
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData

from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

def connect_database():
    '''connect the database
    :return table as dateframe'''
    url = 'mysql+pymysql://root:AI@2019@ai@rm-8vbwj6507z6465505ro.mysql.zhangbei.rds.aliyuncs.com:3306/stu_db'
    engine = create_engine(url)
    session = Session(engine)
    data = pd.read_sql_table(table_name="news_chinese", con=session.connection())
    return data
