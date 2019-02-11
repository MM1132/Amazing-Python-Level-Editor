import pygame

# The tile class itself
class Tile:

    # Initialize all the good shit
    def __init__(self, pos, type, texture):
        self.tilePos = pos
        self.renderPos = [pos[0] * 50, pos[1] * 50]
        self.type = type
        self.texture = texture

    # This function renders a tile onto the map
    def render(self, window, camOffset):
        pygame.draw.rect(window, (255, 0, 0), (self.renderPos[0], self.renderPos[1], 50, 50))