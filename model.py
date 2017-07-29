from __future__ import print_function
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
import generate_data as gd

tsteps = 1
batch_size = 25
epochs = 100
lahead = 1

all_cuisines = gd.get_cuisines()
cuisines, cuisine_scores = gd.get_data_matrix(all_cuisines)
labels = []
index = 1

for cuisine in cuisines:
    labels.append(index)
    index = index + 1
labels = np.asarray(labels, dtype=float)

score_shape = np.reshape(cuisine_scores, (len(cuisine_scores), 1, 1))
output_shape = np.reshape(labels, (len(labels), 1))

print('Input Shape:', score_shape.shape)

print('Data', score_shape)

print('Output shape:', output_shape.shape)

print('Labels', output_shape)

print('Creating Model...');
model = Sequential();
model.add(LSTM(50, input_shape=(tsteps, 1), return_sequences=True,
 stateful=False))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='rmsprop')

for i in range(epochs):
    #print('Epoch', i, '/', epochs)

    model.fit(score_shape, output_shape, batch_size=batch_size,
    epochs=epochs, verbose=1)
    model.reset_states()

predicted_output = model.predict(score_shape, batch_size=batch_size)
print('predicted:', predicted_output)
