import pymysql

connect=pymysql.connect(host='localhost',user='root',password='334455',db='Pedestrian')

try:
    with connect.cursor() as cursor:
        sql='insert into pedestrian.'