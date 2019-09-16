

EPISODES = 100
TIMESTEPS = 100
GAMMA = 0.2

from dql import Dql,AgentActions
from playgame import GameWindow,SnakeEnvState,Reward
import arcade
import numpy as np
from random import *
import collections

def image_preprocess(image):
    image = image.crop((200,200,400,400))
    # image = image.crop((self.x_start,self.y_start,self.x_end,(self.y_end)))
    image = image.convert('LA')
    imagenum = np.array(image)
    imagenum = imagenum[...,:1]

    return imagenum.reshape((200,200))
    #print(imagenum.shape)

    #image.save("./images.png")


def capture_display():
    pass


def main():
    model = Dql()
    current_sequence = collections.deque()
    # for episode in range (0,EPISODES):
    game = GameWindow()
    game.initial_display_state()
    current_sequence.append(image_preprocess(arcade.get_image()))
    epsilon = 0.5
    for t in range (1, TIMESTEPS):
        action_t = None
        if random() < epsilon:
            action_t = random.choice(list(AgentActions))
        else:
            pass
            game.on_key_press(action_t)
            reward_t = game.on_update()
            game.on_draw()
            previous_sequence = current_sequence.copy()
            current_sequence.popleft()
            current_sequence.append(image_preprocess(arcade.get_image()))

            model.store_transition(previous_sequence,action_t,reward_t, current_sequence)

            #Random minibatch
            n = model.get_storage_pos
            random_sample = random.randint(0,n)

            s_prev, s_curr,s_tns = model.get_transition(random_sample)



            if (s_tns[1] == Reward.NEG):
                #THEN s_curr will be terminal
                y = Reward.NEG
            else:
                y = s_tns[1] + GAMMA * np.max(model.prediction(s_curr))

            model.fit(s_prev,y)












if __name__ == "__main__":
    main()
