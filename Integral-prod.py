""" The purpose of this project is to calculate the value of an area behind a graph of a function called probability density function 
	At the moment this program can't be used to calculate de value of areas of any function, only for probability density functions"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
#The interval of the integral, represented by: a = lower bound b = higher bound
a = 0
b = 10
k = 5 # K is equal to the number of "slices" or divisions that we want or the number of rectangles behind the graph
#Note: If you use a higher value in k the program possibly will be a bit slow to show the graph.
#Declaring the funciton
def f(x):
    return 0.1 * np.exp(-0.1 * x)
h = 0  # height of rectangle, in this case f(x)
s = 0  # position of x, initially on the lower bound and moving foward to the higher 
area_total = 0  
total_width = float(b - a)  # Total distance between boundaries
wid_rectangle = float(total_width / k)  # Base of rectangle
x = 0  #Variable to catch the value of width of rectangle

for i in range(k):
    x = wid_rectangle  
    z = np.exp((-1 * (1 / 10)) * s)
    s += x 
    y = f(s)
    area_total += (x * y) 
print(area_total)

n = np.linspace(0, 10, 5001)
plt.plot(n, f(n), color='red')
plt.xlabel("x")
plt.ylabel("y")
v = str(k)
plt.title("Aproximacao por Retangulos: k="+v)

h = comprimento/k
shura = h
l = 0
for i in range(1, k+1):
    c = 0 + l
    d = n[i]
    plt.plot([c, h], [f((h)), f((h))], color='blue')
    #print(h)
    d = h
    l = h
    h = h + shura
    plt.plot([d, d], [0, f(d)], color='blue')
plt.show()
