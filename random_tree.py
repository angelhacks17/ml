import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


LABELS = ["Algerian", "Argentinan", "Australian", "Belgian", "Bosnian","Brazilian", "Cameroonian", "Chilean", "Colombian", "Costa Rican", "Croatian", "Ecuadorian"]
LABELS.append(["English", "French", "German", "Ghanan", "Greek", "Honduran", "Iranian", "Italian", "Ivory Coast", "Japanese", "Mexican", "Netherlands", "Nigerian", "Portugese"])
LABELS.append(["Russian","South Korean", "Spanish", "Swiss", "American", "Uruguayan", "Chinese", "Indian", "Thai", "Turkish", "Cuban", "Ethiopian", "Vietnamese", 'Irish'])
LABELS = np.hstack(LABELS)

def get_correlations(country, data):
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
	print(normalized_perc)
	max = np.max(normalized_perc)
	max_index = normalized_perc.index(max)
	print(LABELS[max_index])


def get_init_data():
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
	return all_data

#get_correlations("England", all_data)
