import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y=np.array([])

for i,u in enumerate(x):
    y=np.append(y,1/(1+10*((u-5)**2)))

plt.plot(x,y)

user=float(input("1-10 arasi sayi girin: "))
result=1/(1+10*((user-5)**2))

plt.scatter(user,result,color="red")
plt.plot([user,user],[0,result],color="red")
plt.plot([0,user],[result,result],color="red")

# plt.axvline(x=user,color="blue")
# plt.axhline(y=result,color="blue")


plt.show()
# if user<0 or user>10:
#     print("hatalı sayı girildi")
# else:
#     print("üyelik derecesi: ",result)






















# import numpy as np 
# import matplotlib.pyplot as plt

# x=np.arange(1,10,0.1)
# y=np.array([])
# z=[]

# for i,tutx in enumerate(x):
#     z.insert(i,(1/(1+pow(tutx-30/5,4))))
#     y=np.append(y,(1/(1+pow(tutx-30/5,4)))) 

# plt.plot(x,z)
# plt.show()

# cevap = "e"

# while(cevap=="e" or cevap=="E"):
#     userx=float(input("1-10 arasi deger gir:"))
#     mx=(1/(1+pow(userx-30/5,4)))
#     print("Üyelik derecesi: ",mx)
#     cevap=input("Devam edecek misiniz (E/e)?")