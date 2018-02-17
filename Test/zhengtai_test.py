import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import random
mu=0
sigma=1
x=np.arange(-5,5,1)
y=norm()
y_s=(y.pdf(x))
print(y_s[5])
# y_s=100*y
# print(y_s)
# y=np.random.normal(mu,sigma,100)
plt.plot(x,y_s)
# print(x,y.pdf(x))
plt.show()
for i in range(0):
    print("pppp")