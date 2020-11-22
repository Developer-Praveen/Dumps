import numpy as np
import matplotlib.pyplot as plt

#Make a Your own Required dataset:
height = [5, 10, 20, 30, 35]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

print (y_pos)

#Create bars
plt.bar(y_pos, height)

#Create names on the x-axis
plt.xticks(y_pos, bars)

#Show graphic
plt.show()