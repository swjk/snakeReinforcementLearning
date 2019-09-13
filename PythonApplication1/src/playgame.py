


from level import level1
import environment as Env

def main():
    game_grid = Env.Grid()
    game_grid.create_grid(level1)
    print(game_grid._cells)
    print(game_grid.find_snake_tail())

if __name__ == "__main__":
    main()
