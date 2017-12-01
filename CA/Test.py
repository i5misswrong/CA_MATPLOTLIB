import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

delta = 0.025
x = np.arange(0, 20.0, delta)
y=np.arange(0,10.0,delta)
X, Y = np.meshgrid(x, y)
# Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z1=np.exp(-((X-3)**2+(Y-5)**2)/2)
# print(x)
# Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# Z = Z2 - Z1  # difference of Gaussians

im = plt.imshow(Z1, interpolation='bilinear', cmap=cm.RdYlGn,
                origin='lower', extent=[0, 20, 0, 10],
                vmax=abs(Z1).max(), vmin=-abs(Z1).max())

plt.show()
# delta = 0.025
# x = y = np.arange(-3.0, 3.0, delta)
# X, Y = np.meshgrid(x, y)
# Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
# Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# Z = Z2 - Z1  # difference of Gaussians
#
# im = plt.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
#                 origin='lower', extent=[-3, 3, -3, 3],
#                 vmax=abs(Z).max(), vmin=-abs(Z).max())
#
# plt.show()
# from collections import Counter
# import random
# import Data,Block
# x=5
# y=8
# coo=[]
# for i in range(x-1,x+2):
#     for j in range(y-1,y+2):
#         c=[i,j]
#         coo.append(c)
# coo.remove([x,y])
# print(coo)
# allPeople=[]
# b3 = Block.Block(0)
# b3.x = 5
# b3.y = 5
# b3.type = True
# allPeople.append(b3)
#
# b4 = Block.Block(1)
# b4.x = 6
# b4.y = 5
# b4.type = True
# allPeople.append(b4)
# for p in allPeople:
#     if p.logo==0:
#         allPeople.remove(p)
# for p in allPeople:
#     print(p.logo)
# ram={1:131.0,2:232.0,3:333.0,4:144.0,5:535.0,6:66.0,7:77.0,8:8338.0,9:299.0}
# # a=random.random()
# # print(a)
# # for i in range(1,10):
# #     ram[i]=random.random()
# #
# # print(ram)
# b=min(ram.items(),key=lambda  x:x[1])[0]
# c=max(ram.items(),key=lambda x:x[1])[0]
# print(b,'mai')
#
# print(c,'max')
# x = { 'apple': 1, 'banana': 2 }
# y = { 'banana': 10, 'pear': 11 }
#
# X,Y = Counter(x), Counter(y)
# z = dict(X+Y)
# print(z)
#
# x1={1:0.0,2:-1000.0,3:0.0,4:200.0,5:100.0,6:0.0,7:100.0,8:20.0,9:0.0}
# y1={1:0.0,2:0.0,3:0.0,4:-1000.0,5:100.0,6:0.0,7:20.0,8:0.0,9:30.0}
# other={1:0.0,2:0.0,3:0.0,4:-1000.0,5:100.0,6:0.0,7:20.0,8:0.0,9:30.0}
# allIn={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
# v1=[]
# v2=[]
# v3=[]
# for i in x1.values():
#     v1.append(i)
# for i in y1.values():
#     v2.append(i)
# for i in other.values():
#     v3.append(i)
#
# print(v1)
# print(v2)
#
# res=list(map(lambda x,y,z:[x+y+z],v1,v2,v3))
# print(res)
# for key in allIn:
#     allIn[key]=res[key-1][0]
#
# print(allIn)




# '''ther is zhshi '''
#
# dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
# ''''''
# dict1= sorted(dic.items(), key=lambda d:d[1], reverse = True)
# print(dict1[0][0])
# k=[]
# v=[]
# for i in dict1:
#     k.append(i[0])
#     v.append(i[1])
#
# print(k)
# print(v)
# fin=dict(map(lambda x,y:[x,y],k,v))
# print(fin)

