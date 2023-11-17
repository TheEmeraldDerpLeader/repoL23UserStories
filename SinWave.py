
from math import sin
from matplotlib  import pyplot as plt

for i in range(0,100,1):
    plt.scatter(i,sin(i/5));
plt.pause(0.001);
input();