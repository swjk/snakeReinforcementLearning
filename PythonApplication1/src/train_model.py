

EPISODES = 100
TIMESTEPS = 100

from dql import Dql,AgentActions
from playgame import GameWindow
import arcade
import numpy as np
from random import *

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
    current_sequence = []
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
            game.on_update()
            game.on_draw()
            current_sequence.append(image_preprocess(arcade.get_image()))
            












if __name__ == "__main__":
    main()
