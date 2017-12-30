import pymysql

connect=pymysql.connect(host='localhost',user='root',password='334455',db='Pedestrian')
case_s=[1,2,3,4,5]
density=[1,2,3,4,5,6,7,8,9]
radius=[1,2,3,4,5,6,7]
step=[1,2,3,4,5]

time=[1,2,3,4,5,6,7,8,9]
surplus=[100,99,98,97,96,90,80,70,60]
v=[1,2,3,4,5,6,7,8,9]
q=[10,20,30,40,50,60,70,80,90]
a=100

try:
    with connect.cursor() as cursor:
        # sql='select * from test'
        # sql='insert into pedestrian.test (case_s,density,radius,step,e_time,surplus,veocity,quantity) VALUES ("&a&",2,3,4,5,6,7,8)'
        # sql='insert into pedestrian.test (case_s) VALUE (%s)'
        for c in case_s:
            for d in density:
                for r in radius:
                    for s in step:
                        sql='insert into pedestrian.test (case_s, density, radius, step, e_time, surplus, veocity, quantity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                        cursor.execute(sql,[c,d,r,s,100,100,100,100])
        # cursor.execute(sql,v[5])
        connect.commit()

finally:
    connect.close()