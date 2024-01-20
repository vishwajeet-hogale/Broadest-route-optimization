import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Dropout, Activation, BatchNormalization
from tensorflow.keras.utils import to_categorical

# Function to create the LSTM model
def create_network(network_input, n_vocab):
    model = Sequential()

    # Embedding layer
    model.add(Embedding(
        input_dim=network_input.shape[1],
        output_dim=150,
        input_length=network_input.shape[1]
    ))

    # LSTM layers
    model.add(LSTM(100, return_sequences=True, recurrent_dropout=0.3))
    model.add(LSTM(50))

    # Batch normalization and dropout
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    # Dense layers
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    # Output layer
    model.add(Dense(n_vocab))
    model.add(Activation('softmax'))

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    return model

# Function to train the model
def train():
    # Read data from CSV
    df = pd.read_csv("RoutesData.csv")

    # Extract features and target
    X = df.iloc[:, 1:]
    Y = X.iloc[:, 3]
    del X[X.columns[3]]

    # Normalize features using MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    X = scaler.fit_transform(X)
    X = pd.DataFrame(X)
    sequences = np.array(X)

    # Convert target to categorical labels
    num_classes = len(set(Y.tolist()))
    labels = to_categorical(Y)

    # Create and compile the LSTM model
    model = create_network(sequences, num_classes)

    # Train the model
    model.fit(sequences, labels, epochs=50, batch_size=4, verbose=1)

if __name__ == "__main__":
    train()
