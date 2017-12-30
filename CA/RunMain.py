import Data,InitPeolple,DrawFirst,Rule,Income
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time

def run_f():
    resultData=[]
    P=0.1
    R=10
    case_s=1
    steps=1
    init = InitPeolple.InitPeople()
    draw = DrawFirst.draw()
    # income = Income.outDirection()
    allPeople = init.creatPeople()
    # allPeople=init.creatAppointPeo()
    allWall = init.creatWall()
    allExit = init.creatExit()
    T=[]
    S=[]
    V=[]
    Q=[]
    Q.append(0)

    evac_time = 0

    while Data.flag:
        move_on_num = 0
        move_off_num = 0
        vector = 0
        for p in allPeople:
            Income.outDirection(p, allPeople)
            direction = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]
            if direction==5:
                move_off_num=move_off_num+1
            else:
                move_on_num=move_on_num+1
            Rule.chickOverAround(p, allPeople)
            Rule.PeopleMove(p, direction)

        draw.drawPeople(allPeople)
        # print(evac_time,"---",len(allPeople),"---",move_on_num/len(allPeople))

        if len(allPeople)==0:
            vector=1
            Data.flag=False
        else:
            vector=move_on_num/len(allPeople)

        T.append(evac_time)
        S.append(len(allPeople))
        V.append(vector)

        evac_time=evac_time+1

    for i in range(len(S) - 1):
        quar = S[i] - S[i + 1]
        Q.append(quar)
    resultData.append(P)
    resultData.append(R)
    resultData.append(case_s)
    resultData.append(steps)
    resultData.append(T)
    resultData.append(S)
    resultData.append(V)
    resultData.append(Q)
    print(resultData)
    print("123")
#
def insertDB():
    pass
if __name__=='__main__':
    run_f()
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




