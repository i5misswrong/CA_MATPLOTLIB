from sympy import *


a=[1,4,5,2,10,100,544]
for i in range(len(a)-1):
    print(a[i]-a[i+1])

# x=Symbol('x')
# y=Symbol('y')
# # print(solve([x+5*y-2,-3*x+6*y-15],[x,y]))
# print(solve([x*((1+94.4*0.035/x) ** y)-1.946,x*((1+94.4*0.036/x) ** y)-2.147],[x,y]))
# print(x)
# print(y)
# class B():
#     def __init__(self,x):
#         self.x=x
#
# a=[1,1,1,1,1]
# bb=[]
# for i in a:
#     b=B(i)
#     bb.append(b)
#
# for i in bb:
#     i.x=i.x+100
#     for j in bb:
#         print(j.x)
#         print("----------")
#
#     print("************")