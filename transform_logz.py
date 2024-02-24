import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

#Enter letter equation here


#transforms add as and when required
u_1 = (le**x_p1)
v_1 = (le**x_p1)

u_2 = np.cos(y_p1)
v_2 = np.sin(y_p1)

u_t1 = np.log((x_p1**2 + y_p1**2)**0.5)
v_t1 = np.arctan(y_p1/x_p1)


# do not edit the graph changes 
# just add new out.plot stattements as and when required
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(-u_t1,v_t1,'k')
# out.plot(x_p2,y_p2,'k')
# out.plot(x_p3,y_p3,'k')
out.axis('off')
plt.show()