import matplotlib.pyplot as plt

x=[0.25,1.25,2.25,3.25,4.25]
y=[50,40,70,80,20]
plt.bar(x,y,label="BMW",width=0.5)

x=[.75,1.75,2.75,3.75,4.75]
y=[80,20,20,50,60]
plt.bar(x,y,label="AUDI",width=0.5)

plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance(kms)")
plt.title("Information")
plt.show()

