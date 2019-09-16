import tensorflow as tf
from tensorflow.python.keras.layers import Input,Dense,Conv3D
from tensorflow.python.keras.models import Sequential
import numpy as np

class Dql(object):

    def __init__(self):
        a = np.memmap("test.dat", dtype='float32', mode="w+", shape=(5,5))
        a[1,2] = 3

        print (a)




    def create_model():
        self.model = Sequential()
        self.model.add(Conv3D(filters= 16, kernel_size=(4,8,8), input_shape =(4,84,84,1), strides=(1,4,4), activation="relu"))
        self.model.add(Conv3D(filters= 32, kernel_size=(4,4,4), strides=(2,2,2), activation="relu"))
        self.model.add(Flatten())
        self.model.add(Dense(256, activation="relu"))
        self.model.add(Dense(2, activation='softmax'))


    def compile_model():
        self.model.compile(loss="mean_squared_error", optimizer='sgd')


    def train_model():
        pass
