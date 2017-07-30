import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


LABELS = ["Algeria", "Argentina", "Australia", "Belgium", "Bosnia and Herzegovina","Brazil", "Cameroon", "Chile", "Colombia", "Costa Rica", "Croatia", "Ecuador"]
LABELS.append(["England", "France", "Germany", "Ghana", "Greece", "Honduras", "Iran", "Italy", "Ivory Coast", "Japan", "Mexico", "Netherlands", "Nigeria", "Portugal"])
LABELS.append(["Russia","South Korea", "Spain", "Switzerland", "United States", "Uruguay", "China", "India", "Thailand", "Turkey", "Cuba", "Ethiopia", "Vietnam", 'Ireland'])
LABELS = np.hstack(LABELS)



df = pd.read_csv('food-world-cup-data.csv', encoding='latin1')
all_data = []
for index, row in df.iterrows():
	user_data = []
	scores = row[3:len(row)-5]
	for score in scores:
		if np.isnan(score):
			user_data.append(0)
		else:
			user_data.append(float(score))
	all_data.append(user_data)
all_data = np.asarray(all_data, dtype=float)
unique_data = np.asarray(all_data[0], dtype=float)
data_user = np.reshape(unique_data, len(LABELS))

print(data_user.shape())

print(len(all_data[0]))
print(len(LABELS))
print(len(all_data[0]))

RandomForestClassifier().fit(data_user, LABELS)