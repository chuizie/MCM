# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dataset with manual values
data = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]])

df = pd.DataFrame(data, columns=["a", "b", "c", "d", "e"])

# Default heatmap with Blues color
p1 = sns.heatmap(df, cmap="Blues")

# Invert the Y axis
plt.gca().invert_yaxis()

# Add x and y axis labels
p1.set_xlabel("X-axis")
p1.set_ylabel("Y-axis")


# Add a title
plt.title("Heatmap with Blues Color")

plt.show()
