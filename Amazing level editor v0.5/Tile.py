import pygame
from TileType import TILES

# The tile class itself
class Tile:
    # Initialize all the good shit
    def __init__(self, pos, type, texture):
        self.tilePos = pos
        self.renderPos = [pos[0] * 50, pos[1] * 50]
        self.type = type
        self.texture = texture

        # TIles own offset
        self.offset = TILES[type][1]

    # This function renders a tile onto the map
    def render(self, window, camOffset):
        window.blit(TILES[self.type][0][self.texture], tuple([self.renderPos[0]+camOffset[0]+self.offset[0], self.renderPos[1]+camOffset[1]+self.offset[1]]))