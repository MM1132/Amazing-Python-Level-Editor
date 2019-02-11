import pygame
from Block import Block
from TileType import DIRT

class Dirt(Block):
    def __init__(self, pos, texture = None):
        self.tilePos = pos
        self.renderPos = [pos[0] * 50, pos[1] * 50]
        self.texture = texture

        self.offset = DIRT[1]

    def render(self, window, camOffset):
        window.blit(DIRT[0][self.texture], tuple([self.renderPos[0]+camOffset[0]+self.offset[0], self.renderPos[1]+camOffset[1]+self.offset[1]]))