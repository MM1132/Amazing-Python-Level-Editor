import pygame
from TileType import TILE
class Tile:
    def __init__(self, pos, type, texture):
        self.pos = pos
        self.blitPos = (self.pos[0]*50, self.pos[1]*50)
        self.type = type
        self.texture = texture
    
    def render(self, window):
        window.blit(TILE[self.type][self.texture], self.blitPos)