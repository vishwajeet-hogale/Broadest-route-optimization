import numpy as np
import pandas as pd
# from music21 import converter, instrument, note, chord,stream
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import BatchNormalization as BatchNorm
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
# from ttensorflow.keras.callbacks import ModelCheckpoint

# def get_unique_values(Y):
#     for i in 

def get_callbacks():
    es = EarlyStopping(monitor = "val_accuracy",min_delta = 0.01,patience = 5,verbose =1)
    model_cp = ModelCheckpoint(filepath="bestmodel.h5",monitor="val_accuracy",save_best_only = True,verbose=1)
    return [es,model_cp]
def create_network(network_input, n_vocab):
    model = Sequential()
    model.add(Embedding(
        input_dim=network_input.shape[1],
        output_dim=300,
        input_length=network_input.shape[1]  # Update this to match the sequence length
    ))
    model.add(LSTM(100, return_sequences=True, recurrent_dropout=0.3,))
    # model.add(LSTM(100))
    model.add(LSTM(50))
    # model.add(LSTM(50, return_sequences=True, recurrent_dropout=0.3,))
    # model.add(LSTM(25, return_sequences=True, recurrent_dropout=0.3,))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Dense(128))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=["accuracy"])

    return model

# def create_network(network_input, n_vocab):
#     model = Sequential()
#     model.add(Embedding(
#         input_dim=network_input.shape[1],
#         output_dim=150,
#         input_length=network_input.shape[1]  # Update this to match the sequence length
#     ))
#     model.add(LSTM(100, return_sequences=True, recurrent_dropout=0.3,))
#     model.add(LSTM(50))
#     model.add(BatchNorm())
#     model.add(Dropout(0.3))
#     model.add(Dense(256))
#     model.add(Activation('relu'))
#     model.add(BatchNorm())
#     model.add(Dropout(0.3))
#     model.add(Dense(n_vocab))
#     model.add(Activation('softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam')

#     return model

def preprocess_for_model(path):
    df = pd.read_csv(path)
    df = df.dropna()
    X = df.iloc[:, 1:]
    Y = X.iloc[:, 3]
    del X[X.columns[3]]
    # max_length = X.shape[1]
    scaler = MinMaxScaler(feature_range=(0, 1))
    X = scaler.fit_transform(X)
    X = pd.DataFrame(X)
    sequences = np.array(X)
    num_classes = len(set(Y.tolist()))
    print(num_classes)
    Y = Y.tolist()
    print(Y)
    # Correct the number of classes in to_categorical
    labels = to_categorical(Y)
    print(labels.shape)
    return sequences,labels,num_classes
def train():
    train_sequences,train_labels,train_num_classes = preprocess_for_model("RoutesData.csv")
    test_sequences,test_labels,num_classes = preprocess_for_model("TestRoutesData.csv")

    model = create_network(train_sequences,train_num_classes + 1)

    # Train the model
    history = model.fit(train_sequences, train_labels, epochs=150, batch_size=4, verbose=1,validation_split = 0.1,callbacks=get_callbacks())
    model.save("MyModel.keras")

if __name__ == "__main__":
    train()
