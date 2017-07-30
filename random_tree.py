import pandas as pd
import numpy as np

df = pd.read_csv('food-world-cup-data.csv', encoding='latin1')
for index, row in df.iterrows():
	print(row)
	break
