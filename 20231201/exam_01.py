import matplotlib.pyplot as plt, random, numpy as np

data_x = []
data_y = []
data_s = []
#for i in range(200):
#    data_x.append(random.randint(10,100))
#    data_y.append(random.randint(10, 100))
#    data_s.append(random.randint(10, 100))

data_x = np.random.randint(10, 100, 200)
data_y = np.random.randint(10, 100, 200)
data_s = np.random.randint(10, 100, 200)

plt.scatter(data_x,data_y
            , s=data_s
            , c=data_x
            , cmap='jet'
            , alpha=0.6)
plt.colorbar()
plt.show()