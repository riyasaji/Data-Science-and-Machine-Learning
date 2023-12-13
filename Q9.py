# Density Chart:-
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
sns.kdeplot(data, fill=True, color='blue', label='Density Plot')
plt.xlabel('X-Axis Label')
plt.ylabel('Density')
plt.title('Density Plot Example')
plt.show()

# Bubble Diagram
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]
sizes = [100, 200, 300, 150, 250]
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Bubble Chart Example')
plt.show()

# Observations
# 1.	A bubble chart assists in visualizing multivariate data by representing three variables simultaneously: X-axis: It represents one numerical variable. Y-axis: It represents another numerical variable. Bubble size: The size of each bubble represents a third numerical variable.
# 2.	2. A density chart, often created using kernel density estimation (KDE), is used to visualize the concentration of data along a single axis.Higher peaks indicate areas of greater data concentration or probability density. These peaks represent modes in the data distribution. The shape of the density curve can provide insights into the central tendency and spread of the data. For example, a unimodal curve suggests one central concentration of data, while a multimodal curve suggests multiple concentrations.
# 3.	3. For the bubble chart, interesting patterns can be observed by examining how the bubble sizes and positions are distributed. However, in the program, there are no obvious patterns or outliers because the dataset used is small
