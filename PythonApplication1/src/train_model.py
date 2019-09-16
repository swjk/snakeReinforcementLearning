

EPISODES = 100
TIMESTEPS = 10
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

    # for episode in range (0,EPISODES):
    current_sequence = collections.deque()
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

            if(reward_t == Reward.NEG):
                break

            #Random minibatch
            n = model.get_storage_pos()
            random_sample = np.random.randint(low=n)
            print ("RandomSample{}".format(random_sample))
            s_prev, s_curr,s_tns = model.get_transition(random_sample)
            print(s_tns)
            if (s_tns[1] == Reward.NEG):

                y = Reward.NEG
            else:
                s_curr = s_curr.reshape(1,4,100,100,1)
                print(model.prediction(s_curr))
                y = s_tns[1] + GAMMA * np.max(model.prediction(s_curr))
            s_prev = s_prev.reshape(1,4,100,100,1)

            target = np.array([0,0,0])
            target[s_tns[0]] = y

            model.fit(s_prev,np.array([target]))

        else:
            current_sequence.append(image_preprocess(arcade.get_image(),t))

            if(reward_t == Reward.NEG):
                break












if __name__ == "__main__":
    main()
