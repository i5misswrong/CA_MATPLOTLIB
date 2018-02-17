import Data,InitPeolple,DrawFirst,Rule,Income
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time
import pymysql


def run_view():
    time_logo=0

    # allPeople = InitPeolple.creatPeople()  # 产生随机行人
    # allPeople=InitPeolple.creatPeople_force_normal()
    # allPeople=InitPeolple.creatPeople_force_fix()
    allPeople=InitPeolple.creatPeople_force_random()
    # allPeople=InitPeolple.creatAppointPeo()#产生指定行人
    # allPeople=InitPeolple.creatAreaPeople()
    # print(len(allPeople))
    # allWall = InitPeolple.creatWall()  # 创建墙壁
    # allExit = InitPeolple.creatExit()  # 创建出口
    DrawFirst.drawPeople(allPeople)
    while Data.flag:#循环开始
        for p in allPeople:#遍历行人
            Income.outDirection(p, allPeople)#计算收益
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
            Rule.chickOverAround(p, allPeople)#检测是否到达出口
            Rule.PeopleMove(p, direction)#行人移动
        DrawFirst.drawPeople(allPeople)
        time_logo = time_logo + 1
        print(time_logo,"\033[4;32;40mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\033[0m")
        # while True:
        #     if Data.figure_pause:
        #         Data.pause_time=1000
        #     else:
        #         Data.pause_time=1
        #     break

        # if time_logo==10:
        #     Data.flag=False
def run_insert(case_s,density,radius,radius_ob,radius_v,force,force_type,peo_view,steps):
    Data.flag=True
    time_logo=0

    if case_s==0:#危险源位置设置
        Data.FX_N=19
    elif case_s==1:
        Data.FX_N = 15
    elif case_s==2:
        Data.FX_N = 10
    elif case_s==3:
        Data.FX_N = 5
    elif case_s==4:
        Data.FX_N = 2

    Data.PEOPLE_DENSYTY=density
    Data.PEOPLE_NUMBER=Data.count_PEOPLE_NUMBER(density)

    Data.FX_SIGMA_2 = radius  # 危险源大小
    Data.FX_R = Data.count_FX_R(radius)  # 影响范围半径
    Data.FX_P = Data.count_FX_P(radius)  # 系数 p越大 高斯函数的圆形越大

    Data.FX_S_SIGMA_2=radius_ob
    Data.FX_S_R=Data.count_FX_S_R(radius_ob)
    Data.FX_S_P=Data.count_FX_S_P(radius_ob)

    Data.FX_S_V=radius_v

    Data.PEOPLE_FORCE=force

    if force_type==0:# fix
        allPeople = InitPeolple.creatPeople_force_fix()
    else: #random
        allPeople=InitPeolple.creatPeople_force_random()

    Data.PEOPLE_FAN_R=peo_view

    while Data.flag:#循环开始
        for p in allPeople:#遍历行人
            Income.outDirection(p, allPeople)#计算收益
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
            Rule.chickOverAround(p, allPeople)#检测是否到达出口
            Rule.PeopleMove(p, direction)#行人移动
        if len(allPeople)==0:
            Data.flag=False
        time_logo = time_logo + 1
    # print(time_logo)
    # print("\033[4;32;40mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\033[0m")

    return time_logo

def run_force_test(double_r,steps):
    time_logo=0
    Data.PEOPLE_FORCE=50
    Data.FX_S_SIGMA_2=double_r
    Data.FX_S_R = 2 * np.sqrt(Data.FX_S_SIGMA_2)
    Data.FX_S_P = 2 * Data.FX_S_SIGMA_2
    allPeople = InitPeolple.creatPeople()  # 产生随机行人
    # allPeople=InitPeolple.creatAppointPeo()#产生指定行人
    # allPeople=InitPeolple.creatAreaPeople()
    # print(len(allPeople))
    # allWall = InitPeolple.creatWall()  # 创建墙壁
    # allExit = InitPeolple.creatExit()  # 创建出口
    # DrawFirst.drawPeople(allPeople)
    while Data.flag:#循环开始
        for p in allPeople:#遍历行人
            Income.outDirection(p, allPeople)#计算收益
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
            Rule.chickOverAround(p, allPeople)#检测是否到达出口
            Rule.PeopleMove(p, direction)#行人移动
        # DrawFirst.drawPeople(allPeople)
        time_logo = time_logo + 1
        # print(time_logo,"\033[4;32;40mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\033[0m")
        if len(allPeople)==0:
            Data.flag=False
    allData=[]
    allData.append(double_r)
    allData.append(steps)
    allData.append(time_logo)
    return allData
def insertDB_force_test():
    connect = pymysql.connect(host='localhost', user='root', password='334455', db='pedestrian')  # 获取链接

    '''设置循环参数'''
    list_case = [0,1,2]#危险源位置
    list_density = [0.8,0.9]#行人密度
    list_radius_core = [9,18,27]#危险源半径
    list_radius_ob=[30,40,50,60,70,80,90,100]#危险源边缘半径
    list_radius_v_increase=[0]#危险源边缘增长速度
    list_force=[0,10,20,30,40,50,60,70,80,90,100]#行人影响力
    list_force_tyoe=[1,2]#行人影响力类型
    list_people_view=[10]#行人视野半径
    list_steps = [0,1,2,3,4]
    '''参数设置结束'''
    try:
        with connect.cursor() as cursor:  # 打开游标
            for l_c in list_case:
                for l_d in list_density:
                    for l_r_c in list_radius_core:
                        for l_r_o in list_radius_ob:
                            for l_r_v_i in list_radius_v_increase:
                                for l_f in list_force:
                                    for l_f_t in list_force_tyoe:
                                        for l_p_v in list_people_view:
                                            for l_s in list_steps:
                                                time_logo=run_insert(l_c,l_d,l_r_c,l_r_o,l_r_v_i,l_f,l_f_t,l_p_v,l_s)
                                                sql='insert into pedestrian.danger_double (case_s,density,radius,radius_ob,radius_v,force_s,force_type,peo_view,steps,time_logo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                                cursor.execute(sql,[l_c,l_d,l_r_c,l_r_o,l_r_v_i,l_f,l_f_t,l_p_v,l_s,time_logo])
                                                connect.commit()
                                                print("case:",l_c,"-density:",l_d,"-核心半径:",l_r_c,"-边缘半径:",l_r_o,"-增长速度:",l_r_v_i,"-影响力:",l_f,"-影响力类型:",l_f_t,"-视野半径:",l_p_v,"-步数:",l_s,"----当前时间:",time_logo)
    finally:  # 如果发生异常，关闭数据库
        connect.close()
def run_insert_old(case_s,P,R,steps):
    resultData=[]#返回总列表
    if case_s==0:#危险源位置设置
        Data.FX_N=19
    elif case_s==1:
        Data.FX_N = 15
    elif case_s==2:
        Data.FX_N = 10
    elif case_s==3:
        Data.FX_N = 5
    elif case_s==4:
        Data.FX_N = 2
    Data.PEOPLE_DENSYTY=P#行人密度
    Data.PEOPLE_NUMBER=int(Data.ROOM_N*Data.ROOM_M*Data.PEOPLE_DENSYTY)#行人数量
    Data.FX_SIGMA_2=R#危险源大小
    Data.FX_R = 2 * np.sqrt(Data.FX_SIGMA_2)  # 影响范围半径
    Data.FX_P = 2 * Data.FX_SIGMA_2  # 系数 p越大 高斯函数的圆形越大

    # init = InitPeolple.InitPeople()#实例化 产生行人类
    # draw = DrawFirst.draw()#实例化 画图类
    # income = Income.outDirection()
    allPeople = InitPeolple.creatPeople()#产生随机行人
    # allPeople=init.creatAppointPeo()#产生指定行人
    allWall = InitPeolple.creatWall()#创建墙壁
    allExit = InitPeolple.creatExit()#创建出口

    T=[]#疏散时间
    S=[]#剩余行人
    V=[]#行人速度
    Q=[]#出口流量
    Q.append(0)#将出口流量[0]设为0 Q列表少一个数

    evac_time = 0#疏散时间

    while Data.flag:#循环开始
        move_on_num = 0#本次时间步移动的行人
        move_off_num = 0#本次时间步静止的行人
        vector = 0#本次时间步行人速度
        for p in allPeople:#遍历行人
            Income.outDirection(p, allPeople)#计算收益
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
            if direction==5:#如果行人静止
                move_off_num=move_off_num+1#计数器+1
            else:
                move_on_num=move_on_num+1#计数器+1
            Rule.chickOverAround(p, allPeople)#检测是否到达出口
            Rule.PeopleMove(p, direction)#行人移动

        # draw.drawPeople(allPeople)#绘制行人
        # print(evac_time,"---",len(allPeople),"---",move_on_num/len(allPeople))

        if len(allPeople)==0:#如果行人全部疏散完毕
            vector=1#速度设为1
            Data.flag=False#循环标志--停止
        else:
            vector=move_on_num/len(allPeople)#行人速度=移动的行人/总行人
        if vector>1:#如果行人速度>1
            vector=1.0#设置为1

        T.append(evac_time)#将疏散时间添加到T
        S.append(len(allPeople))#将剩余行人添加到S
        V.append(vector)#将行人速度添加到V

        evac_time=evac_time+1#疏散时间+1

    for i in range(len(S) - 1):#遍历行人
        quar = S[i] - S[i + 1]#出口流量=上一步的行人总数-下一步的行人总数
        Q.append(quar)#将出口流量添加到Q

    '''将各种参数添加到返回列表'''
    resultData.append(case_s)
    resultData.append(P)
    resultData.append(R)
    resultData.append(steps)
    resultData.append(T)
    resultData.append(S)
    resultData.append(V)
    resultData.append(Q)


    return resultData
def insertDB():
    connect = pymysql.connect(host='localhost', user='root', password='334455', db='Pedestrian')  # 获取链接

    '''设置循环参数'''
    list_case = [0, 1, 2, 3, 4]
    list_density = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    list_radius = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    list_steps = [0, 1, 2, 3, 4]

    try:
        with connect.cursor() as cursor:  # 打开游标
            for l_c in list_case:  # 开始循环
                for l_d in list_density:
                    for l_r in list_radius:
                        for l_s in list_steps:
                            allData = []  # 接受参数
                            allData = run_insert_old(l_c, l_d, l_r, l_s)  # 运行主函数

                            '''接受各种参数'''
                            case_s = allData[0]
                            density = allData[1]
                            radius = allData[2]
                            steps = allData[3]
                            time_s = allData[4]
                            surplus = allData[5]
                            veocity = allData[6]
                            quantity = allData[7]

                            print('当前case=', case_s, '---', '密度=', density, '---', '半径=', radius, '执行到第', steps, '步')
                            Data.flag = True  # 设置循环标识符
                            '''设置sql语句'''
                            sql = 'insert into pedestrian.danger_one (case_s, P, R, steps, time_s, surplus, V, Q) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                            for i in range(len(time_s)):  # 循环将其写入数据库
                                cursor.execute(sql, [case_s, density, radius, steps, time_s[i], surplus[i], veocity[i],
                                                     quantity[i]])
                            connect.commit()  # 数据库执行
    finally:  # 如果发生异常，关闭数据库
        connect.close()
if __name__=='__main__':
    # insertDB()
    # run_view()
    insertDB_force_test()
    #
    # # allData=run_f()
    # print(allData)
    #
    #
    # print(len(time_s))

# for l_f in list_double_r:
#     for l_s in list_steps:
#         allData = []  # 接受参数
#         allData = run_force_test(l_f, l_s)  # 运行主函数
#
#         '''接受各种参数'''
#         force = allData[0]
#         steps = allData[1]
#         T = allData[2]
#         # case_s = allData[0]
#         # density = allData[1]
#         # radius = allData[2]
#         # steps = allData[3]
#         # time_s = allData[4]
#         # surplus = allData[5]
#         # veocity = allData[6]
#         # quantity = allData[7]
#
#         # print('当前case=', case_s, '---', '密度=', density, '---', '半径=', radius, '执行到第', steps, '步')
#         print("force=", force, '---', "steps=", steps, '---', "time_s=", T)
#         Data.flag = True  # 设置循环标识符
#         '''设置sql语句'''
#         # sql = 'insert into pedestrian.danger_one (case_s, P, R, steps, time_s, surplus, V, Q) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
#         sql = "insert into pedestrian.force_time (forces,steps,T) values (%s,%s,%s)"
#         cursor.execute(sql, [force, steps, T])
#         # for i in range(len(T)):  # 循环将其写入数据库
#         # cursor.execute(sql, [case_s, density, radius, steps, time_s[i], surplus[i], veocity[i],
#         #                      quantity[i]])
#         connect.commit()  # 数据库执行
# list_case=[2]
    # list_density=[0.1]
    # list_radius=[33,36]
    # list_steps=[0]

# while Data.flag:
#     for p in allPeople:
#         defineDirection.countDefine(p)
#         isCrash.isNextNull(p,allPeople)
#         move.moveRight(p)
#         if not p.type:
#
#             print(p.nextNull)
#
#     draw.drawPeople(allPeople)

# while True:
#
#     for p in allPeople:
#         move.moveRight(p)
#
#     print(allPeople[0].x)
#     draw.drawPeople(allPeople)
#     draw.drawWallAndExit()
#     # plt.show()
#     # plt.pause(1)
# # print(allPeople)
# def run_f():
#
#     init=InitPeolple.InitPeople()
#     draw=DrawFirst.draw()
#     # move=Rule.PeopleMove()
#     income=Income.outDirection()
#     allPeople=init.creatPeople()
#     # allPeople=init.creatAppointPeo()
#     allWall=init.creatWall()
#     allExit=init.creatExit()
#     # while Data.flag:
#
#     # for p in allPeople:
#     #     income.outDirection(p,allPeople)
#     #     direction=max(p.allInComeBySort.items(),key=lambda  x:x[1])[0]
#     #     print('direction ==',direction)
#     while Data.flag:
#         for p in allPeople:
#             income.outDirection(p,allPeople)
#
#             direction=max(p.allInComeBySort.items(),key=lambda  x:x[1])[0]
#             Rule.chickOverAround(p,allPeople)
#             Rule.PeopleMove(p,direction)
#             # print(p.grendIncome)
#             # print(p.isInGrend)
#             # print(p.allInComeBySort)
#         draw.drawPeople(allPeople)




