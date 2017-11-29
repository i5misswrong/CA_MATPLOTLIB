import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data


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
    def drawPeople(self,P=[]):
        plt.clf()
        R_x=[]
        R_y=[]
        L_x=[]
        L_y=[]
        for p in P:
            if p.logo==Data.LOGO_PEOPLE:

                if p.type:
                    R_x.append(p.x)
                    R_y.append(p.y)
                else:
                    L_x.append(p.x)
                    L_y.append(p.y)
            # R_x.append(p[0])
            # R_y.append(p[1])
        # plt.figure(figsize=(10,6))
        plt.subplot(1,1,1)
        plt.scatter(R_x,R_y,c='r')
        plt.scatter(L_x,L_y,c='b')
        draw.drawWallAndExit(self)
        # plt.show()
        closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])
        closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')
        closeFigbutton.on_clicked(draw.closeFigure)
        plt.pause(1)

    def closeFigure(event):
        plt.close()
        Data.flag=False


    def drawWallAndExit(self):

        plt.plot([0,Data.ROOM_M],[0,0],'b-')# down
        plt.plot([0,Data.ROOM_M],[Data.ROOM_N,Data.ROOM_N],'b-')# up
        plt.plot([0,0],[0,Data.ROOM_N],'y--')#left and right
        plt.plot([Data.ROOM_M,Data.ROOM_M],[0,Data.ROOM_N],'y--')
        # plt.show()