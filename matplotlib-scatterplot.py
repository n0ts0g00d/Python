import matplotlib.pyplot as plt

# scatterplot

x=[1,1.5,2,2.5,3,3.5,3.6]
y=[7.5,8,8.5,9,9.5,10,10.5]
plt.scatter(x,y,label='high income low saving')
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x1,y1,label='low income high saving')
plt.legend()
plt.xlabel("Saving*100")
plt.ylabel("Income*1000")
plt.title("Scatterplot")
plt.show()