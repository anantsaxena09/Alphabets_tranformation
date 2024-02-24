
import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

#A
x_p1 = 1 + t
y_p1 = 3*t

x_p2 = 2 + t
y_p2 = 3 - 3*t

x_p3 = 1.5 + t
y_p3 = 1.5 + 0*t

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#B
x_p1 = 1 + np.cos(pe/2 - pe*t)
y_p1 = 3 + np.sin(pe/2 - pe*t)

x_p2 = 1 + np.cos(pe/2 - pe*t)
y_p2 = 1 + np.sin(pe/2 - pe*t)

x_p3 = 1 + 0*t
y_p3 = 4*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#C
x_p1 = 3 + np.cos(5*pe/3 - (4*pe/3)*t)
y_p1 = 2 + np.sin(5*pe/3 - (4*pe/3)*t)
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.axis('off')
plt.show()
#D
x_p1 = 1 + 0*t
y_p1 = 4*t

x_p2 = 1 + 2*(np.cos(pe/2 - pe*t))
y_p2 = 2 + 2*(np.sin(pe/2 - pe*t)) 
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#E
y_p1 = 3*t
x_p1 = 0*t + 1

y_p2 = 0*t + 3
x_p2 = t/2 + 1

y_p3 = 0*t + 3/2
x_p3 = t/2 +1

y_p4 = 0*t + 0
x_p4 = t/2 + 1
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.plot(x_p4,y_p4,'k')
out.axis('off')
plt.show()

#F
y_p1 = 3*t
x_p1 = 0*t + 1

y_p2 = 0*t + 3/2
x_p2 = t/2 +1

y_p3 = 0*t + 3
x_p3 = t/2 + 1
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()

#G
x_p1 = 2 + 2*np.cos(pe/2+ 3*pe*t/2)
y_p1 = 2 + 2*np.sin(pe/2+ 3*pe*t/2)

x_p2 = 2.5 + 1.5*t
y_p2 = 2 + 0*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()
#H
x_p1 = 1 + 0*t
y_p1 = 4*t

x_p2 = 3 + 0*t
y_p2 = 4*t

x_p3 = 1 + 2*t
y_p3 = 2 + 0*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#I
x_p1 = 2 + 0*t
y_p1 = 4*t

x_p2 = 1 + 2*t
y_p2 = 4 + 0*t

x_p3 = 1 + 2*t
y_p3 = 0 + 0*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()

#J
x_p1 = 2 + 0*t
y_p1 = 1 + 3*t

x_p2 = 1 + np.cos(-pe*t)
y_p2 = 1 + np.sin(-pe*t)
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()
#K
x_p1 = 1 + 0*t
y_p1 = 4*t

x_p2 = 1 + 2*t
y_p2 = 2 + 2*t

x_p3 = 1 + 2*t
y_p3 = 2 - 2*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()

#L
y_p1 = 4*t
x_p1 = 0*t + 1

y_p2 = 0*t + 0
x_p2 = 1 + 2*t

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()
#M
y_p1 = t + 1
x_p1 = 0*t + 1

y_p2 = -t/2 + 2
x_p2 = 0.5*t/2 + 1

y_p3 = t/2 + 1.5
x_p3 = 0.5*t/2 + 1.25

y_p4 = t + 1
x_p4 = 0*t + 1.5
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.plot(x_p4,y_p4,'k')
out.axis('off')
plt.show()
#N

y_p1 = t + 1
x_p1 = 0*t + 1

y_p2 = -t + 2
x_p2 = 0.5*t + 1


y_p3 = t + 1
x_p3 = 0*t + 1.5
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#O

x_p1 = 2 + 2*np.cos(2*pe*t)
y_p1 = 2 + 2*np.sin(2*pe*t)
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.axis('off')
plt.show()
# P
x_p1 = 1 + np.cos(pe/2 - pe*t)
y_p1 = 3 + np.sin(pe/2 - pe*t)
y_p2 = t*4
x_p2 = 1 + 0*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()

# Q
x_p1 = 2 + 2*np.cos(2*pe*t)
y_p1 = 2 + 2*np.sin(2*pe*t)

x_p2 = 3 + t
y_p2 = 1 - t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()

# R
x_p1 = 1 + np.cos(pe/2 - pe*t)
y_p1 = 3 + np.sin(pe/2 - pe*t)
y_p2 = t*4
x_p2 = 1 + 0*t
y_p3 = 2 - 2*t
x_p3 = 1 + 1*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#S
x_p1 = 2 + np.cos(3*pe*t/2)
y_p1 = 3 + np.sin(3*pe*t/2)

x_p2 = 2 + np.cos(-pe + 3*pe*t/2)
y_p2 = 1 + np.sin(-pe + 3*pe*t/2)
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()

#T
x_p1 = 2 + 0*t
y_p1 = t*4
x_p2 = 1 + 2*t
y_p2 = 4 + 0*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()

#U
x_p1 = 2 + np.cos( - pe*t)
y_p1 = 1 + np.sin( - pe*t)

x_p2 = 1 + 0*t
y_p2 = 1 + 3*t

x_p3 = 3 + 0*t
y_p3 = 1 + 3*t

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()
#V- feed
x_p1 = 2+t
y_p1= 3*t

x_p2 = 2-t
y_p2= 3*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()
#W

x_p1 = 1-t 
y_p1= 3*t

x_p2= 3+t
y_p2= 3*t

x_p3 = 1+t
y_p3 = 1.5*t

x_p4= 3-t 
y_p4= 1.5*t

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.plot(x_p4,y_p4,'k')
out.axis('off')
plt.show()

#X
x_p1 = 1+2*t
y_p1 = 3*t

x_p2 = 3-2*t 
y_p2 = 3*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.axis('off')
plt.show()
#Y
x_p1 =2 + 0*t
y_p1 =1.5-1.5*t

x_p2 = 2+t
y_p2 = 1.5+1.5*t

x_p3 = 2-t
y_p3=1.5+1.5*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()

#Z
x_p1 = 1+2*t
y_p1 = 3 + 0*t

x_p2 = 1+2*t 
y_p2 = 0*t

x_p3 = 1+2*t 
y_p3 = 3*t
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()