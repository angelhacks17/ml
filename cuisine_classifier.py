import pandas as pd
import numpy as np
import tensorflow as tf


LABELS = ["Algerian", "Argentinan", "Australian", "Belgian", "Bosnian","Brazilian", "Cameroonian", "Chilean", "Colombian", "Costa Rican", "Croatian", "Ecuadorian"]
LABELS.append(["English", "French", "German", "Ghanan", "Greek", "Honduran", "Iranian", "Italian", "Ivory Coast", "Japanese", "Mexican", "Netherlands", "Nigerian", "Portugese"])
LABELS.append(["Russian","South Korean", "Spanish", "Swiss", "American", "Uruguayan", "Chinese", "Indian", "Thai", "Turkish", "Cuban", "Ethiopian", "Vietnamese", 'Irish'])
LABELS = np.hstack(LABELS)

def get_data():
	df = pd.read_csv('food-world-cup-data.csv', encoding='latin1')
	all_data = []
	for index, row in df.iterrows():
		user_data = []
		scores = row[3:len(row)-5]
		for score in scores:
			if np.isnan(score):
				user_data.append(0)
			else:
				user_data.append(float(score)/5)
		all_data.append(user_data)
	all_data = np.asarray(all_data, dtype=float)
	return all_data

data = get_data()
hidden_units = 20
visible_units = len(LABELS)
vb = tf.placeholder("float", [visible_units])
hb = tf.placeholder("float", [hidden_units])
W = tf.placeholder("float", [visible_units, hidden_units])
v0 = tf.placeholder("float", [none, visible_units])
_h0 = tf.nn.sigmoid(tf.matmul(v0, W) + hb)
h0 = tf.nn.relu(tf.sign(_h0 - tf.random_uniform(tf.shape(_h0))))
_v1 = tf.nn.sigmoid(tf.matmul(h0, tf.transpose(W)) + vb)
v1 = tf.nn.relu(tf.sign(_v1 - tf.random_uniform(tf.shape(_v1))))
h1 = tf.nn.sigmoid(tf.matmul(v1, W) + hb)






