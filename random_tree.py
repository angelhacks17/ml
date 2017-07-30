import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


LABELS = ["Algeria", "Argentina", "Australia", "Belgium", "Bosnia and Herzegovina","Brazil", "Cameroon", "Chile", "Colombia", "Costa Rica", "Croatia", "Ecuador"]
LABELS.append(["England", "France", "Germany", "Ghana", "Greece", "Honduras", "Iran", "Italy", "Ivory Coast", "Japan", "Mexico", "Netherlands", "Nigeria", "Portugal"])
LABELS.append(["Russia","South Korea", "Spain", "Switzerland", "United States", "Uruguay", "China", "India", "Thailand", "Turkey", "Cuba", "Ethiopia", "Vietnam", 'Ireland'])
LABELS = np.hstack(LABELS)
AVOID = ["F"]


def get_correlations(country, data):
	# print(AVOID)
	all_cor = []
	label_list = LABELS.tolist()
	index = label_list.index(country)
	org_score = []
	for dat in data:
		org_score.append(dat[index])
	i = 0
	while(i < 40):
		cur_score = []
		for x in data:
			cur_score.append(x[i])
		if index == i:
			all_cor.append([[-1,-1],[-1,-1]])
		elif index != i:
			all_cor.append(np.corrcoef(org_score, cur_score))
		i = i+1
	normalized_perc = []
	for x in all_cor:
		val = x[0][1]
		normalized_perc.append(val)
	# print(normalized_perc)
	while(True):
		max = np.max(normalized_perc)
		max_index = normalized_perc.index(max)
		if LABELS[max_index] in AVOID:
			normalized_perc[max_index] = -1
		else:
			if len(AVOID) > 5:
				del AVOID[0:1]
				print(AVOID)
				# AVOID = hi
			break
	print(LABELS[max_index])
	print("\n")
	return LABELS[max_index], normalized_perc


def train(label):
	AVOID.append(label)
	print(label)
	new_cuisine, prob_values  = get_correlations(label, all_data)	
	train(new_cuisine)




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

list1 = []
list2 = []
train("India")
