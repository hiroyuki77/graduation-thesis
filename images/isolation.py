import sys
import numpy as np
import matplotlib.pyplot as plt

data = [[50, 50], [15, 30]]

num_sample = 2
num_item_per_sample = 2

legend_labels = ["85% disk I/O share, need 50%", "15% disk I/O share, need 30%"]

colors = ["r", "b"]

width = 0.25
margin = 0.2
block = width * num_sample + margin
ind = np.arange(num_item_per_sample) * block

for i in range(num_sample):
	plt.bar(ind + width * i, 
	data[i], 
	width, 
	color=colors[i], 
	label=legend_labels[i])

xlabels = ["throttle", "isolation"]
xlocs = ind + width * num_sample / 2.
plt.xticks(xlocs, xlabels)
plt.xlim(-margin, ind[-1] + width * num_sample + margin)
plt.ylim(0, 100)
plt.ylabel('disk I/O usage[%]')

plt.legend(prop={'size' : 18}, loc="upper right")
plt.grid(True)

plt.savefig("./isolation.png", bbox_inches="tight")
plt.show()

