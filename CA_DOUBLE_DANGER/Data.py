import numpy as np
flag=True
figure_pause=False #绘图程序暂停状态

ROOM_M=40
ROOM_N=20


LOGO_NULL=0
LOGO_PEOPLE=1
LOGO_WALL=10
LOGO_EXIT=100

PEOPLE_DENSYTY=0.1
PEOPLE_NUMBER=int(ROOM_N*ROOM_M*PEOPLE_DENSYTY)
# PEOPLE_NUMBER=100
'''二维高斯分布函数'''
FX_M=20#x位移   高斯函数原点
FX_N=10#y位移
FX_SIGMA_2=20#sigma平方
FX_R=2*np.sqrt(FX_SIGMA_2) #影响范围半径
FX_P=2*FX_SIGMA_2#系数 p越大 高斯函数的圆形越大
def countFX(X,Y):#函数表达式
    return np.exp(-((X-FX_M)**2+(Y-FX_N)**2)/FX_P)

#--------双层危险源参数----------------------
FX_S_SIGMA_2=33
FX_S_R=2*np.sqrt(FX_S_SIGMA_2)
FX_S_P=2*FX_S_SIGMA_2



#-----------行人扇形视野参数----------------
PEOPLE_FAN_R=10 #行人扇形视野半径
PEOPLE_FAN_A=120 #行人扇形角度

