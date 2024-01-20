import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Given data
data = [
    [4, 4, 7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ...],
    [1, 4, 7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ...],
    [3, 4, 7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ...],
    [2, 4, 7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ...],
    [6, 4, 7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ...],
    [8, 8, 9, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ...],
]

# Extracting relevant information
# sequences = [item[3] for item in data]
# labels = [item[2] for item in data]

# Convert sequences and labels to numpy arrays
sequences = np.array(sequences)
labels = np.array(labels)

# Define the LSTM model
embedding_dim = 50  # Adjust as needed
max_length = len(sequences[0])

model = Sequential()
model.add(Embedding(input_dim=len(sequences[0]), output_dim=embedding_dim, input_length=max_length))
model.add(LSTM(100))  # Adjust the number of units as needed
model.add(Dense(1, activation='sigmoid'))  # Adjust output layer accordingly

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(sequences, labels, epochs=10, batch_size=1)  # Adjust epochs and batch_size as needed
