
import arcade
import random

WIDTH = 600
HEIGHT = 600
SCREEN_TITLE = "snake"
RATE = 5


class Item(arcade.Sprite):
    def __init__(self):
        super().__init__("./texture.jpg",1)
        self.position = (100,100)
        self.size = 20
        self.height = 20
        self.width = 20

    def changeLocation(self):
       self.position =(random.randint(20,WIDTH-20), random.randint(20, HEIGHT-20))

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.position[0],self.position[0] + self.size, self.position[1], self.position[1] - self.size, [100,100,100])

    def update(self,x):
        return


class SnakeTail(arcade.Sprite):
    def __init__(self,position):
        super().__init__("./texture.jpg",1)
        self.position = position
        self.size = 20
        self.height = 20
        self.width = 20


    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.position[0],self.position[0] + self.size, self.position[1], self.position[1] - self.size, [200,200,200])



class Snake():
    def __init__(self):
        self.length = 1
        self.sprites = arcade.SpriteList()
        self.possibleMovements = [(0,-1), (1,0), (0,1),  (-1,0)]
        self.direction = self.possibleMovements[1];
        self.directionIndex = 1
        self.size = 20
        self.speed = 10
        self.sprites.append(self.createSprite((300,300)))
        self.lastPosition = (0,0)

    def createSprite(self, pos):
        newSprite = SnakeTail(pos)
        newSprite.position = pos
        return newSprite



    def increaseLength(self):
        self.length += 1
        self.sprites.append(self.createSprite(self.lastPosition))

    def changeSnakeDirection(self, symbol):
        if symbol == arcade.key.LEFT and (self.directionIndex == 0):
            self.directionIndex = (self.directionIndex -1 ) % len(self.possibleMovements)
        elif symbol == arcade.key.RIGHT and (self.directionIndex == 0):
            self.directionIndex = (self.directionIndex + 1) % len(self.possibleMovements)
        elif symbol == arcade.key.LEFT and (self.directionIndex == 2):
            self.directionIndex = (self.directionIndex + 1) % len(self.possibleMovements)
        elif symbol == arcade.key.RIGHT and (self.directionIndex == 2):
            self.directionIndex = (self.directionIndex - 1) % len(self.possibleMovements)
        elif symbol == arcade.key.UP and (self.directionIndex == 1):
            self.directionIndex = (self.directionIndex + 1) % len(self.possibleMovements)
        elif symbol == arcade.key.DOWN and (self.directionIndex == 1):
            self.directionIndex = (self.directionIndex - 1) % len(self.possibleMovements)
        elif symbol == arcade.key.UP and (self.directionIndex == 3):
            self.directionIndex = (self.directionIndex - 1) % len(self.possibleMovements)
        elif symbol == arcade.key.DOWN and (self.directionIndex == 3):
            self.directionIndex = (self.directionIndex + 1) % len(self.possibleMovements)


        self.direction = self.possibleMovements[self.directionIndex]

    def draw(self):
        self.sprites.draw()

    def update(self,x):

        frontSprite = self.sprites.pop()
        self.lastPosition = frontSprite.position
        self.sprites.append(frontSprite)
        self.sprites.append(self.createSprite((frontSprite.position[0] + self.direction[0]*self.speed, frontSprite.position[1] + self.direction[1]*self.speed )))
        self.sprites.remove(self.sprites[0])


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, SCREEN_TITLE)


    def start_game(self):
        self.snake = Snake()
        self.item = Item()


    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.item.draw()



    def on_key_press(self,symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT or symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.snake.changeSnakeDirection(symbol)

    def update(self,x):
        if arcade.check_for_collision_with_list(self.item, self.snake.sprites):
            self.snake.update(x)
            self.item.update(x)
            self.snake.increaseLength()
            self.item.changeLocation()
        else:
            self.snake.update(x)
            self.item.update(x)




def main():
    window = GameWindow()
    window.start_game()
    arcade.run()


if __name__ == "__main__":
    main()
