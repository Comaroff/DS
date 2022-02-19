import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # задает стиль графика

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
print()
print('*****')
print("Mean height:       ", heights.mean())
print("Standart deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())
print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')

plt.xlabel('height (cm)')
plt.ylabel('number')
