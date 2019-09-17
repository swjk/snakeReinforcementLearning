

EPISODES = 1000
TIMESTEPS = 100
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
    #image.save("./images/{}{}.png".format("image",timestep))


    return imagenum.reshape((100,100))



def capture_display():
    pass


def main():
    model = Dql()

    for episode in range (0,EPISODES):
        current_sequence = collections.deque()
        game = GameWindow()
        game.initial_display_state()
        current_sequence.append(image_preprocess(arcade.get_image(),0))
        epsilon = 0.3
        for t in range (1, TIMESTEPS):
            print("Timestep{}".format(t))
            action_t = None
            if random.random() < epsilon or len(current_sequence) < 4:
                action_t = random.choice(list(AgentActions))
            else:
                current_t = np.array([current_sequence[0],current_sequence[1],current_sequence[2],current_sequence[3]])
                current_t = current_t.reshape(1,4,100,100,1)
                result_t = model.prediction(current_t)
                print(np.argmax(result_t))
                action_t = AgentActions(np.argmax(result_t))

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
                batch_input = np.array([]).reshape(0,4,100,100,1)
                batch_output= np.array([]).reshape(0,3)
                for i in range (0, min(n,20)):
                    random_sample = np.random.randint(low=n)
                    s_prev, s_curr,s_tns = model.get_transition(random_sample)
                    if (s_tns[1] == Reward.NEG):
                        y = Reward.NEG
                    else:
                        s_curr = s_curr.reshape(1,4,100,100,1)
                        y = s_tns[1] + GAMMA * np.max(model.prediction(s_curr))
                    s_prev = s_prev.reshape(1,4,100,100,1)

                    target = np.array([0,0,0])
                    target[s_tns[0]] = y
                    batch_output = np.vstack((batch_output,target))
                    batch_input = np.vstack((batch_input, s_prev))
                model.fit(batch_input,batch_output)

            else:
                current_sequence.append(image_preprocess(arcade.get_image(),t))

                if(reward_t == Reward.NEG):
                    break
        arcade.close_window()


if __name__ == "__main__":
    main()
