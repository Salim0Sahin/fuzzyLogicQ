import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-501,501,1)
y=np.array([])

for i,u in enumerate(x):
    if u<200:
        y=np.append(y,1)
    elif u>500:
        y=np.append(y,0)
    elif 200<= u <=500:
        y=np.append(y,(500-u)/300)
    else:
        break
plt.plot(x,y)
plt.xlabel("Mesafe")
plt.show()
