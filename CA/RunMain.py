import Data,InitPeolple,DrawFirst,Rule,Income
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time

init=InitPeolple.InitPeople()
draw=DrawFirst.draw()
# move=Rule.PeopleMove()
income=Income.outDirection()
# allPeople=init.creatPeople()
allPeople=init.creatAppointPeo()
allWall=init.creatWall()
allExit=init.creatExit()
# while Data.flag:

for p in allPeople:
    income.outDirection(p,allPeople)
    direction=max(p.allInComeBySort.items(),key=lambda  x:x[1])[0]
    print('direction ==',direction)
while Data.flag:
    for p in allPeople:
        income.outDirection(p,allPeople)

        direction=max(p.allInComeBySort.items(),key=lambda  x:x[1])[0]
        Rule.chickOverAround(p,allPeople)
        Rule.PeopleMove(p,direction)
        # print(p.allInComeBySort)
    draw.drawPeople(allPeople)
# for p in allPeople:
#     defineDirection.countDefine(p)
#     isCrash.isNextNull(p, allPeople)
#     print(p.nextNull)
#     move.moveRight(p)
#     # if not p.type:
# plt.figure(figsize=(10,6))


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




