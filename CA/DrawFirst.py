import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data
import matplotlib.cm as cm
import matplotlib.mlab as mlab


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

class draw():
    '''绘制行人  主绘图方法'''
    def drawPeople(self,P=[]):
        plt.clf()#清除数据
        draw.drawFile(self)#绘制高斯函数
        R_x=[]#向右移动的行人的x坐标
        R_y=[]#y坐标
        L_x=[]#向左移动的行人的x坐标
        L_y=[]#y坐标
        for p in P:#遍历行人列表
            if p.logo==Data.LOGO_PEOPLE:#此行可以省略？
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
        plt.scatter(R_x,R_y,c='r')#绘制行人--散点图
        plt.scatter(L_x,L_y,c='b')


        draw.drawWallAndExit(self)#绘制墙壁和出口
        # plt.show()
        '''由于无法右上角关闭 加了个关闭按钮'''
        closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])#关闭按钮
        closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')#按钮样式
        closeFigbutton.on_clicked(draw.closeFigure)#按钮按下去的动作
        plt.pause(1)#暂停1s
    '''关闭按钮动作'''
    def closeFigure(event):
        plt.close()#将窗口关闭
        Data.flag=False#循环标记为Fasle

    '''绘制墙壁和出口'''
    def drawWallAndExit(self):
        '''墙壁为实线'''
        plt.plot([0,Data.ROOM_M],[0,0],'b-')# down
        plt.plot([0,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],'b-')# up
        '''出口为虚线'''
        plt.plot([0,0],[0,Data.ROOM_N],'y--')#left and right
        plt.plot([Data.ROOM_M,Data.ROOM_M],[0,Data.ROOM_N],'y--')
        # plt.show()
    '''绘制高斯函数'''
    def drawFile(self):
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
        plt.plot(c_x,c_y,c='r')
        plt.plot(c_x,c_y_2,c='r')


        # plt.show()