import random
import Data,Block
class InitPeople():
    '''初始化随机行人'''
    def creatPeople(self):
        allBlock=[]#用于存放格子
        allPeople=[]#用于存放行人
        '''将所有格子全部存入列表'''
        for i in range(1,Data.ROOM_M):
            for j in range(1,Data.ROOM_N):
                b=Block.Block(1)
                b.x=i
                b.y=j
                if j>Data.ROOM_N/2:
                    b.type=False
                else:
                    b.type=True
                allBlock.append(b)
        '''随机排序'''
        random.shuffle(allBlock)
        '''取前N个'''
        '''可有效防止无限产生随机数'''
        allPeople=allBlock[:10]
        return allPeople

    '''产生指定行人'''
    def creatAppointPeo(self):
        allPeople=[]
        # b1=Block.Block(1)
        # b1.x=3
        # b1.y=5
        # b1.type=True
        # allPeople.append(b1)
        #
        # b2=Block.Block(1)
        # b2.x=4
        # b2.y=5
        # b2.type=False
        # allPeople.append(b2)

        b3 = Block.Block(1)
        b3.x = 18
        b3.y = 10
        b3.type = True
        allPeople.append(b3)

        # b4 = Block.Block(1)
        # b4.x = 6
        # b4.y = 5
        # b4.type = True
        # allPeople.append(b4)

        return allPeople
    '''产生墙壁'''
    def creatWall(self):
        allWall=[]
        for i in range(5):
            D=[i,0]
            U=[i,2]
            allWall.append(D)
            allWall.append(U)
        return allWall
    '''产生出口'''
    def creatExit(self):
        allExit=[]
        for i in range(3):
            L=[0,i]
            R=[4,i]
            allExit.append(L)
            allExit.append(R)
        return allExit



