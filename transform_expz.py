
import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

# Enter letter equations here
x_p1 = 1+2*t
y_p1 = 3 + 0*t

x_p2 = 1+2*t 
y_p2 = 0*t

x_p3 = 1+2*t 
y_p3 = 3*t
#transforms add as and when required
u_1 = (le**x_p1)
v_1 = (le**x_p1)

u_2 = np.cos(y_p1)
v_2 = np.sin(y_p1)

u_t1 = u_1*u_2
v_t1 = v_1*v_2

u_3 = (le**x_p2)
v_3 = (le**x_p2)

u_4 = np.cos(y_p2)
v_4 = np.sin(y_p2)

u_t2 = u_3*u_4
v_t2 = v_3*v_4

u_5 = (le**x_p3)
v_5 = (le**x_p3)

u_6 = np.cos(y_p3)
v_6 = np.sin(y_p3)

u_t3 = u_5*u_6
v_t3 = v_5*v_6

# u_7 = (le**x_p4)
# v_7 = (le**x_p4)

# u_8 = np.cos(y_p4)
# v_8 = np.sin(y_p4)

# u_t4 = u_7*u_8
# v_t4 = v_7*v_8
# do not edit the graph changes 
# just add new out.plot stattements as and when required
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(u_t1,v_t1,'k')
out.plot(u_t2,v_t2,'k')
out.plot(u_t3,v_t3,'k')
# out.plot(u_t4,v_t4,'k')
out.axis('off')
plt.show()

