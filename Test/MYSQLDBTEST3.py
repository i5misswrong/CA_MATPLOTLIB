import pymysql

connect=pymysql.connect(host='localhost',user='root',password='334455',db='pedestrian')
print(connect)
case_s=[1,2,3,4,5]
density=[1,2,3,4,5,6,7,8,9]
radius=[1,2,3,4,5,6,7]
step=[1,2,3,4,5]


try:
    with connect.cursor() as cursor:
        # sql='select * from test'
        # sql='insert into pedestrian.test (case_s,density,radius,step,e_time,surplus,veocity,quantity) VALUES ("&a&",2,3,4,5,6,7,8)'
        # sql='insert into pedestrian.test (case_s) VALUE (%s)'
        sql="insert into pedestrian.force_time (forces) VALUES (10)"
        # sql='select * from pedestrian.force_times_test'
        cursor.execute(sql)
        # cursor.execute(sql,v[5])
        connect.commit()

finally:
    connect.close()