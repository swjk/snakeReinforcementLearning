class GameState(object):
    GAME_RUNNING = 0
    GAME_OVER = 1


class SnakeEnvState(object):
    COLLISION = 0
    EATEN = 1
    NORM = 2


class Reward(object):
    POS = 1
    NEG = -1
    NORM = 0
