import matplotlib.pyplot as plt
import csv
from pylab import *

x = []
y = []

with open('Data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

xlim(0, 50)
ylim(0, 110)
plt.ylabel('PDR(%)',fontsize=15)
plt.xlabel('Distance (m)',fontsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.title('PDR as a function of link length',fontsize=20)

plt.plot(x,y,'*', markersize=15)
plt.show()
plt.legend()
