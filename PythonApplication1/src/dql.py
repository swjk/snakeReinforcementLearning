import tensorflow as tf
from tensorflow.python.keras.layers import Input,Dense,Conv3D
from tensorflow.python.keras.models import Sequential
import numpy as np
from enum import Enum

N = 1000

class AgentActions(Enum):
    LEFT  = 0
    NO_ACTION  = 1
    RIGHT = 2

class Dql(object):

    def __init__(self):
        self.sequences_prev = np.memmap("sequences_prev.dat", dtype='float32', mode="w+", shape=(N,200,800))
        self.sequences_curr = np.memmap("sequences_curr.dat", dtype='float32', mode="w+", shape=(N,200,800))
        self.sequences_tns = np.memmap("sequences_prev.dat", dtype='float32', mode="w+", shape=(N,1,2))
        self.nextpos = 0


    def store_transition(o_s,action_t,reward_t,c_s):
        #200*4+200*4+1
        sequence_prev = np.concatenate(o_s[0],o_s[1],o_s[2],o_s[3])
        sequence_curr = np.concatenate(c_s[0],c_s[1],c_s[2],c_s[3])
        sequence_tns = np.array([action_t, reward_t])

        self.sequences_prev[self.nextpos] = sequence_prev
        self.sequences_curr[self.nextpos] = sequence_curr
        self.sequences_tns[self.nextpos] = sequence_tns
        self.nextpos += 1

    def get_transition(index):
        sequence_prev = self.sequences_prev[index]
        sequence_curr = self.sequences_curr[index]
        sequence_tns  = self.sequences_tns[index]

        return sequence_prev, sequence_curr, sequence_tns

    def get_storage_pos():
        return self.nextpos

    def create_model():
        self.model = Sequential()
        self.model.add(Conv3D(filters= 16, kernel_size=(4,8,8), input_shape =(4,84,84,1), strides=(1,4,4), activation="relu"))
        self.model.add(Conv3D(filters= 32, kernel_size=(4,4,4), strides=(2,2,2), activation="relu"))
        self.model.add(Flatten())
        self.model.add(Dense(256, activation="relu"))
        self.model.add(Dense(3, activation='softmax'))


    def compile_model():
        self.model.compile(loss="mean_squared_error", optimizer='sgd')


    def fit(input,expected_output):
        self.model.fit(input,expected_output)

    def prediction(data):
        return self.model.predict(data)
