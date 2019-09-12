


from level import level1
import environment as Env

def main():
    game_grid = Env.Grid()
    game_grid.createGrid(level1)
    print(game_grid._cells)

if __name__ == "__main__":
    main()
