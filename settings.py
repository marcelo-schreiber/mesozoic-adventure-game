# 0 - rgb(255,255,255)
# 1 - rgb(0,0,0)

FPS = 30
TILE_SIZE = 64
WIDTH, HEIGHT = 16 * TILE_SIZE, 16 * TILE_SIZE
PLAYER_HP = 1
PLAYER_NAME = 'blue'

arrayMap_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 0, 0, 7, 0, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
              [1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1],
              [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
              [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
              [1, 0, 1, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 1, 0, 1],
              [1, 5, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 6, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

arrayMap_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
              [1, 0, 1, 0, 5, 1, 0, 1, 1, 0, 1, 5, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
              [1, 1, 1, 0, 1, 0, 0, 4, 0, 0, 0, 1, 0, 1, 1, 1],
              [1, 2, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 2, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 0, 1],
              [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
              [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

arrayMaps = [arrayMap_1, arrayMap_2]

# 0 - rgb(255,255,255)
# 1 - rgb(0,0,0)
