

EPISODES = 100
TIMESTEPS = 6
GAMMA = 0.2

from dql import Dql,AgentActions
from playgame import GameWindow,SnakeEnvState,Reward
import arcade
import numpy as np
import random
import collections

def image_preprocess(image, timestep):
    image = image.crop((250,250,350,350))
    # image = image.crop((self.x_start,self.y_start,self.x_end,(self.y_end)))
    image = image.convert('LA')
    imagenum = np.array(image)
    imagenum = imagenum[...,:1]
    image.save("./images/{}{}.png".format("image",timestep))


    return imagenum.reshape((100,100))



def capture_display():
    pass


def main():
    model = Dql()
    current_sequence = collections.deque()
    # for episode in range (0,EPISODES):
    game = GameWindow()
    game.initial_display_state()
    current_sequence.append(image_preprocess(arcade.get_image(),0))
    epsilon = 0.5
    for t in range (1, TIMESTEPS):
        print("Timestep{}".format(t))
        #TODO: CHANGE ACTION_T WITH ELSE INSERT
        action_t = random.choice(list(AgentActions))
        if random.random() < epsilon:
            action_t = random.choice(list(AgentActions))
        else:
            pass
        game.on_key_press(action_t,None)
        reward_t = game.on_update(1)
        game.on_draw()

        print("DequeLen{}".format(len(current_sequence)))

        if len(current_sequence) == 4:
            previous_sequence = current_sequence.copy()
            current_sequence.popleft()
            current_sequence.append(image_preprocess(arcade.get_image(),t))
            model.store_transition(previous_sequence,action_t,reward_t, current_sequence)
        else:
            current_sequence.append(image_preprocess(arcade.get_image(),t))
    print("Finshed")
        #Random minibatch
        # n = model.get_storage_pos
        # random_sample = random.randint(0,n)
        #
        # s_prev, s_curr,s_tns = model.get_transition(random_sample)
        #
        #
        #
        # if (s_tns[1] == Reward.NEG):
        #     #THEN s_curr will be terminal
        #     y = Reward.NEG
        # else:
        #     y = s_tns[1] + GAMMA * np.max(model.prediction(s_curr))
        #
        # model.fit(s_prev,y)
        #
        #
        #
        #








if __name__ == "__main__":
    main()
