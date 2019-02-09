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

    # This function renders a tile onto the map
    def render(self, window, offset):
        window.blit(TILES[self.type][self.texture], tuple([self.renderPos[0]+offset[0], self.renderPos[1]+offset[1]]))