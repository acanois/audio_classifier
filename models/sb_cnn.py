from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

def build_model():
    model = Sequential()

    model.add(Conv2D(filters=24, kernel_size=(5, 5)))
    model.add(MaxPooling2D(pool_size=(4, 2), activation='relu'))
    model.add(Conv2D(filters=48, kernel_size=(5, 5)))
    model.add(MaxPooling2D(pool_size=(4, 2), activation='relu'))
    model.add(Conv2D(filters=48, kernel_size=(5, 5)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model
