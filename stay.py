#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import pymysql
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb() 
import MySQLdb

df = pd.read_excel("C:/Users/dohyeon/Desktop/데이터베이스/프로젝트/경기도검색순위/관광숙박업체현황1.xlsx", engine="openpyxl")

df = df.drop(columns = ['인허가일자', '인허가취소일자'])
df = df.drop(columns = ['자본금', '부대시설내역', '시설규모(㎡)'])
df = df.drop(columns = ['방송시설유무', '발전시설유무', '안내소유무'])
df = df.drop(columns = ['놀이시설수', '놀이기구수내역', '시설면적', '회의실동시수용인원수', '기념품종류명', '좌석수', '무대면적', '선박제원내용'])
df = df.drop(columns = ['선박수', '선박총톤수', '영문상호주소', '지하층수', '지상층수', '주변환경명', '총층수'])
df = df.drop(columns = ['지역구분명', '문화사업자구분명', '문화체육업종명', '업태구분명정보', '소재지우편번호', '도로명우편번호'])
df = df.drop(columns = ['영업상태구분코드', '폐업일자', '소재지면적정보'])

df = df[df['영업상태명'] == '영업중']

engine = create_engine("mysql+mysqldb://user1:12345@localhost:3306/project", encoding='utf-8')
con = engine.connect()

df.rename(columns={'영업상태명':'영업상태', '소재지시설전화번호':'전화번호', '소재지도로명주소':'도로명주소', '소재지지번주소':'지번주소', 'WGS84위도':'위도', 'WGS84경도':'경도'}, inplace = True)

df = df.astype({ '영업상태':'category'})

df.to_sql(name='stay', con=engine, if_exists='fail', index=False)


