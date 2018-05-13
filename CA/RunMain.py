import Data,InitPeolple,DrawFirst,Rule,Income
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time
import math
import pymysql


def run_view():
    evac_time = 0#疏散时间
    Data.FX_R=6
    Data.FX_P = math.pow(6, 2) / 2


    result_speed=[]
    allPeople=InitPeolple.creatPeople()
    DrawFirst.drawPeople(allPeople)
    while Data.flag:#循环开始
        move_on=0
        move_all=0

        for p in allPeople:#遍历行人
            Income.outDirection(p, allPeople)#计算收益
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
            if direction!=5:
                move_on=move_on+1
            move_all=move_all+1
            Rule.PeopleMove(p, direction)  # 行人移动
            Rule.chickOverAround(p, allPeople)#检测是否到达出口

        DrawFirst.drawPeople(allPeople)
        speed=move_on/move_all
        result_speed.append(speed)
        evac_time=evac_time+1#疏散时间+1
        if evac_time==15:
            Data.flag=False
        print('当前时间步：',evac_time)
    print(result_speed)

def run_insert(par_case,par_density,par_radius):
    Data.flag=True
    evac_time = 0#疏散时间
    if par_case==1:
        Data.FX_N=19
    elif par_case==2:
        Data.FX_N = 15
    else:
        Data.FX_N = 10

    Data.PEOPLE_DENSYTY=par_density
    Data.PEOPLE_NUMBER = int(Data.ROOM_N * Data.ROOM_M * par_density)

    Data.FX_R=par_radius
    Data.FX_P = math.pow(par_radius, 2) / 2

    result_all=[]
    result_speed=[]
    result_time=[]
    allPeople=InitPeolple.creatPeople()
    while Data.flag:#循环开始
        move_on = 0
        move_all = 0
        for p in allPeople:#遍历行人
            Income.outDirection(p, allPeople)#计算收益
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
            if direction!=5:
                move_on=move_on+1
            move_all=move_all+1
            Rule.PeopleMove(p, direction)  # 行人移动
            Rule.chickOverAround(p, allPeople)#检测是否到达出口
        if len(allPeople)==0:
            Data.flag=False
        speed = move_on / move_all
        result_speed.append(speed)
        result_time.append(evac_time,)
        evac_time=evac_time+1#疏散时间+1
    result_all.append(result_time)
    result_all.append(result_speed)
    return result_all

#
# def insert_db():
#     connect=pymysql.connect(host='localhost',user='root',password='334455',db='pedestrian_fix_20180506')
#     list_case=[1,2,3]
#     list_density=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
#     list_radius=[4,6,8,10]
#     list_steps=[0,1,2,3,4]
#     try:
#         with connect.cursor() as cursor:
#             for l_c in list_case:
#                 for l_d in list_density:
#                     for l_r in list_radius:
#                         for l_s in list_steps:
#                             time_s=run_insert(l_c,l_d,l_r)
#                             print('case=',l_c,'----density=',l_d,'----radius=',l_r,'----steps=',l_s,'----times=',time_s)
#                             sql = 'insert into pedestrian_fix_20180506.density_and_time (case_s, density, radius, steps, time_s) VALUES (%s,%s,%s,%s,%s)'
#                             cursor.execute(sql,[l_c,l_d,l_r,l_s,time_s])
#                             connect.commit()
#     finally:
#         connect.close()



def insert_db():
    connect=pymysql.connect(host='localhost',user='root',password='334455',db='pedestrian_fix_20180506')
    list_case=[1,2,3]
    list_density=[0.5,0.9]
    list_radius=[6,10]
    list_steps=[5,6,7,8,9,10,11,12]
    try:
        with connect.cursor() as cursor:
            for l_c in list_case:
                for l_d in list_density:
                    for l_r in list_radius:
                        for l_s in list_steps:
                            all_res=run_insert(l_c,l_d,l_r)
                            print('case=',l_c,'----density=',l_d,'----radius=',l_r,'----steps=',l_s,'----times=')
                            sql = 'insert into pedestrian_fix_20180506.main_speed (case_s, density, radius, step_s, time_s, v) VALUES (%s,%s,%s,%s,%s,%s)'
                            # print(all_res[1][5])
                            # print('asvsss')
                            for i_t in range(len(all_res[0])):
                                cursor.execute(sql,[l_c,l_d,l_r,l_s,all_res[0][i_t],all_res[1][i_t]])
                                connect.commit()
    finally:
        connect.close()

if __name__=='__main__':
    # run_view()
    insert_db()

    # def db_insert():
# connect = pymysql.connect(host='localhost', user='root', password='334455', db='Pedestrian')  # 获取链接
#
#     '''设置循环参数'''
#     list_case = [0, 1, 2, 3, 4]
#     list_density = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
#     list_radius = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
#     list_steps = [0, 1, 2, 3, 4]
#
#     try:
#         with connect.cursor() as cursor:  # 打开游标
#             for l_c in list_case:  # 开始循环
#                 for l_d in list_density:
#                     for l_r in list_radius:
#                         for l_s in list_steps:
#                             allData = []  # 接受参数
#                             allData = run_f(l_c, l_d, l_r, l_s)  # 运行主函数
#
#                             '''接受各种参数'''
#                             case_s = allData[0]
#                             density = allData[1]
#                             radius = allData[2]
#                             steps = allData[3]
#                             time_s = allData[4]
#                             surplus = allData[5]
#                             veocity = allData[6]
#                             quantity = allData[7]
#
#                             print('当前case=', case_s, '---', '密度=', density, '---', '半径=', radius, '执行到第', steps, '步')
#                             Data.flag = True  # 设置循环标识符
#                             '''设置sql语句'''
#                             sql = 'insert into pedestrian.danger_one (case_s, P, R, steps, time_s, surplus, V, Q) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
#                             for i in range(len(time_s)):  # 循环将其写入数据库
#                                 cursor.execute(sql, [case_s, density, radius, steps, time_s[i], surplus[i], veocity[i],
#                                                      quantity[i]])
#                             connect.commit()  # 数据库执行
#     finally:  # 如果发生异常，关闭数据库
#         connect.close()
    #
    # # allData=run_f()
    # print(allData)
    #
    #
    # print(len(time_s))
# def run_f(case_s,P,R,steps):
#     resultData=[]#返回总列表
#     if case_s==0:#危险源位置设置
#         Data.FX_N=19
#     elif case_s==1:
#         Data.FX_N = 15
#     elif case_s==2:
#         Data.FX_N = 10
#     elif case_s==3:
#         Data.FX_N = 5
#     elif case_s==4:
#         Data.FX_N = 2
#     Data.PEOPLE_DENSYTY=P#行人密度
#     Data.PEOPLE_NUMBER=int(Data.ROOM_N*Data.ROOM_M*Data.PEOPLE_DENSYTY)#行人数量
#     Data.FX_SIGMA_2=R#危险源大小
#     Data.FX_R = 2 * np.sqrt(Data.FX_SIGMA_2)  # 影响范围半径
#     Data.FX_P = 2 * Data.FX_SIGMA_2  # 系数 p越大 高斯函数的圆形越大
#
#     init = InitPeolple.InitPeople()#实例化 产生行人类
#     # draw = DrawFirst.draw()#实例化 画图类
#     # income = Income.outDirection()
#     allPeople = init.creatPeople()#产生随机行人
#     # allPeople=init.creatAppointPeo()#产生指定行人
#     allWall = init.creatWall()#创建墙壁
#     allExit = init.creatExit()#创建出口
#
#     T=[]#疏散时间
#     S=[]#剩余行人
#     V=[]#行人速度
#     Q=[]#出口流量
#     Q.append(0)#将出口流量[0]设为0 Q列表少一个数
#
#     evac_time = 0#疏散时间
#
#     while Data.flag:#循环开始
#         move_on_num = 0#本次时间步移动的行人
#         move_off_num = 0#本次时间步静止的行人
#         vector = 0#本次时间步行人速度
#         for p in allPeople:#遍历行人
#             Income.outDirection(p, allPeople)#计算收益
#             direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]#获取方向
#             if direction==5:#如果行人静止
#                 move_off_num=move_off_num+1#计数器+1
#             else:
#                 move_on_num=move_on_num+1#计数器+1
#             Rule.chickOverAround(p, allPeople)#检测是否到达出口
#             Rule.PeopleMove(p, direction)#行人移动
#
#         # draw.drawPeople(allPeople)#绘制行人
#         # print(evac_time,"---",len(allPeople),"---",move_on_num/len(allPeople))
#
#         if len(allPeople)==0:#如果行人全部疏散完毕
#             vector=1#速度设为1
#             Data.flag=False#循环标志--停止
#         else:
#             vector=move_on_num/len(allPeople)#行人速度=移动的行人/总行人
#         if vector>1:#如果行人速度>1
#             vector=1.0#设置为1
#
#         T.append(evac_time)#将疏散时间添加到T
#         S.append(len(allPeople))#将剩余行人添加到S
#         V.append(vector)#将行人速度添加到V
#
#         evac_time=evac_time+1#疏散时间+1
#
#     for i in range(len(S) - 1):#遍历行人
#         quar = S[i] - S[i + 1]#出口流量=上一步的行人总数-下一步的行人总数
#         Q.append(quar)#将出口流量添加到Q
#
#     '''将各种参数添加到返回列表'''
#     resultData.append(case_s)
#     resultData.append(P)
#     resultData.append(R)
#     resultData.append(steps)
#     resultData.append(T)
#     resultData.append(S)
#     resultData.append(V)
#     resultData.append(Q)
#
#
#     return resultData
#
#
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




