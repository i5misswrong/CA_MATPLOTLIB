import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import time

# N = 1000
# x = np.random.randn(N)
# y = np.random.randn(N)
# plt.scatter(x, y)
# plt.show()


# plt.plot([0,10],[0,0],'b-')
# plt.plot([0,10],[10,10],'b-')
# plt.plot([0,0],[0,10],'y--')
# plt.plot([10,10],[0,10],'y--')
# plt.show()

'''绘制行人  主绘图方法'''
def drawPeople(P=[]):
    plt.clf()#清除数据
    drawFile()#绘制高斯函数
    # draw.drawSecondFile(self)
    R_x=[]#向右移动的行人的x坐标
    R_y=[]#y坐标
    L_x=[]#向左移动的行人的x坐标
    L_y=[]#y坐标
    G_x=[]#位于危险源内的行人
    G_y=[]
    G_x_r=[]#离开危险源-朝右走的行人
    G_y_r=[]
    G_x_l=[]#离开危险源-朝左走的行人
    G_y_l=[]
    for p in P:#遍历行人列表
        if p.logo==Data.LOGO_PEOPLE:#此行可以省略？
            if p.isInGrend:
                if p.isNewDefine==1:
                    G_x_l.append(p.x)
                    G_y_l.append(p.y)
                elif p.isNewDefine==2:
                    G_x_r.append(p.x)
                    G_y_r.append(p.y)
                else:
                    G_x.append(p.x)
                    G_y.append(p.y)
            else:
                if p.type:#如果行人方向为 【右】
                    R_x.append(p.x)#添加x坐标
                    R_y.append(p.y)#添加y坐标
                else:#如果行人方向为【左】
                    L_x.append(p.x)
                    L_y.append(p.y)
        # R_x.append(p[0])
        # R_y.append(p[1])
    # plt.figure(figsize=(10,6))
    plt.subplot(1,1,1)#绘图板布局  不知道怎么取消这一行
    plt.scatter(G_x,G_y,c='k',marker='s')
    plt.scatter(L_x, L_y, c='r',marker='<')  # 绘制行人--散点图
    plt.scatter(R_x, R_y, c='b',marker='>')
    plt.scatter(G_x_l,G_y_l,c='k',marker='<')
    plt.scatter(G_x_r, G_y_r, c='k', marker='>')

    drawWallAndExit()#绘制墙壁和出口
    # plt.show()
    '''由于无法右上角关闭 加了个关闭按钮'''
    closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])#关闭按钮
    closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')#按钮样式
    closeFigbutton.on_clicked(closeFigure)#按钮按下去的动作
    # pauseFig=plt.axes([0.2,0.025,0.1,0.04])
    # pauseFigbutton=Button(pauseFig,'pause',hovercolor='0.5')
    # pauseFigbutton.on_clicked(draw.pauseFigure)
    while Data.pause_flag:
        plt.pause(1)  # 暂停1s
    plt.pause(0.01)#暂停1s
'''关闭按钮动作'''
def closeFigure(event):
    plt.close()#将窗口关闭
    Data.flag=False#循环标记为Fasle
'''绘制墙壁和出口'''
def drawWallAndExit():
    '''墙壁为实线'''
    plt.plot([0,Data.ROOM_M],[0,0],'b-')# down
    plt.plot([0,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],'b-')# up
    '''出口为虚线'''
    plt.plot([0,0],[0,Data.ROOM_N],'y--')#left and right
    plt.plot([Data.ROOM_M,Data.ROOM_M],[0,Data.ROOM_N],'y--')
    # plt.show()
'''绘制高斯函数'''
def drawFile():
    delta = 0.1#网格间隔
    x = np.arange(0,Data.ROOM_M, delta)#产生x序列
    y = np.arange(0,Data.ROOM_N, delta)#产生y序列
    X, Y = np.meshgrid(x, y)#生成网格
    # Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    # Z1 = np.exp(-((X - 3) ** 2 + (Y - 5) ** 2) / 2)
    Z1=Data.countFX(X,Y)#计算函数
    # print(x)
    # Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    # Z = Z2 - Z1  # difference of Gaussians
    '''绘制图形'''
    im = plt.imshow(Z1, interpolation='bilinear', cmap=cm.RdYlGn,
                    origin='lower', extent=[-2, Data.ROOM_M+2, -2, Data.ROOM_N+2],
                    vmax=abs(Z1).max(), vmin=-abs(Z1).max())

    c_x=np.arange(0,Data.ROOM_M,0.001)
    c_y=Data.FX_N+np.sqrt(Data.FX_R**2-(c_x-Data.FX_M)**2)
    c_y_2 = Data.FX_N - np.sqrt(Data.FX_R ** 2 - (c_x - Data.FX_M) ** 2)
    # print(Data.FX_R)
    plt.plot(c_x,c_y,c='r')
    plt.plot(c_x,c_y_2,c='r')


    # plt.show()
def drawSecondFile():
    c_x = np.arange(0, Data.ROOM_M, 0.001)
    c_y = Data.FX_N + np.sqrt(Data.FX_S_R ** 2 - (c_x - Data.FX_M) ** 2)
    c_y_2 = Data.FX_N - np.sqrt(Data.FX_S_R ** 2 - (c_x - Data.FX_M) ** 2)
    # print(Data.FX_R)
    plt.plot(c_x, c_y, c='y')
    plt.plot(c_x, c_y_2, c='y')