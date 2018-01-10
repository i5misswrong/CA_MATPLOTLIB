import pymysql

connect = pymysql.connect(host='localhost', user='root', password='334455', db='Pedestrian')#获取链接
steps=[0,1,2,3,4]
P=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
cases=[0,1,2,3,4]
try:

    with connect.cursor() as cursor:  # 打开游标
        for c in cases:
            for d in P:
                print("density=",d,end="--")
                for i in steps:
                    sql = "select count(surplus) from pedestrian.danger_one where case_s='%s' and P='%s' and R=33 and steps='%s'"
                    cursor.execute(sql,[c,d,i])
                    result=cursor.fetchall()
                    print(result[0][0],"-",end="")
                print("")
            print("------------------")
finally:
    connect.close()