import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,100,1)
y=np.array([])

for i,u in enumerate(x):
    if u<40 or u>60:
        y=np.append(y,0)
    elif 40<= u <=50:
        y=np.append(y,(u-40)/10)
    elif 50<= u <=60:
        y=np.append(y,(60-u)/10)
    else:
        break

plt.plot(x,y)
plt.show()


