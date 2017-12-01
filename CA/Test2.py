from sympy import *

x=Symbol('x')
y=Symbol('y')
# print(solve([x+5*y-2,-3*x+6*y-15],[x,y]))
print(solve([x*((1+94.4*0.035/x) ** y)-1.946,x*((1+94.4*0.036/x) ** y)-2.147],[x,y]))
print(x)
print(y)
