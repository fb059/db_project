import pandas as pd
import numpy as np
import pymysql
from pymysql import ProgrammingError

data = pd.read_excel('경기도관광검색순위.xlsx')
data = data.fillna('None')
data = data.where(pd.notnull(data), None)
print(data)

mydb = pymysql.connect(
  host = "localhost",
  user = "qwon",
  password = "rozhdwl99!",
  database = "db_hw"
)
curs = mydb.cursor(pymysql.cursors.DictCursor)

sql = 'insert into 경기도관광검색순위 (순위, 관광지명, 도로명주소, 중분류카테고리, 소분류카테고리, 검색건수) values(%s,%s,%s,%s,%s,%s)'

for idx in range(len(data)):
	curs.execute(sql, tuple(data.values[idx]))

mydb.commit()

curs.close()
mydb.close()
