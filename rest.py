import pandas as pd
import numpy as np
import pymysql
from pymysql import ProgrammingError 

data = pd.read_csv('안심식당정보.csv', encoding='cp949') 
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

sql = 'insert into 안심식당 (안심식당번호, 시도명, 시군구명 , 사업장명, 정제도로명주소, 정제지번주소, 상세주소, 업종명, 업종상세명, 
전화번호, 선정여부구분, 취소일자, 비고사항, 수정일, 정제우편번호, 정제WGS84위도, 정제WGS84경도) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

for idx in range(len(data)):
	curs.execute(sql, tuple(data.values[idx]))   

mydb.commit()

curs.close()
mydb.close()
