import numpy as np
from random import randint


def get_cuisines(file):
	return ["Indian", "Chinese"]

def get_data_matrix(cuisines):
	cuisine_scores = []
	for cuisine in cuisines:
		cuisine_scores.append(randint(0, 5))
	cuisine_scores = np.asarray(cuisine_scores, dtype = float)
	return cuisines, cuisine_scores




"""
Main
"""

if __name__ == "__main__":
    all_cuisines = get_cuisines("hello")
    print(get_data_matrix(all_cuisines))

