from collections import Counter
import random
import Data,Block
allPeople=[]
b3 = Block.Block(0)
b3.x = 5
b3.y = 5
b3.type = True
allPeople.append(b3)

b4 = Block.Block(1)
b4.x = 6
b4.y = 5
b4.type = True
allPeople.append(b4)
for p in allPeople:
    if p.logo==0:
        allPeople.remove(p)
for p in allPeople:
    print(p.logo)
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

