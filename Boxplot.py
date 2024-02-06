# libraries & dataset
import seaborn as sns
import csv
import numpy as np
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset('iris')

sns.boxplot( x = df['species'], y = df['petal_length'])
plt.show()





