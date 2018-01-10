import pymysql

connect = pymysql.connect(host='localhost', user='root', password='334455', db='Pedestrian')#获取链接
steps=[0,1,2,3,4]
P=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
cases=[0,1,2,3,4]
try:
    with connect.cursor() as cursor:  # 打开游标
        sql="select time_s,V,Q from pedestrian.danger_one where case_s=2 and R=27 and P=0.5 and steps='%s'"
        all_v=[]
        for s in steps:
            cursor.execute(sql,[s])
            reult=cursor.fetchall()
            v_list=[]
            for i in reult:
                v_list.append(i[2])
            all_v.append(v_list)
        len_v_in=[]
        for i in all_v:
            len_v_in.append(len(i))

        for m in range(min(len_v_in)):
            sige = 0
            for j in all_v:
                sige=sige+j[m]
            print(sige/5)
finally:
    connect.close()
