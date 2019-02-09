import pygame
from Tile import Tile
class Map:
    def __init__(self):
        self.tileSize = 50
        file = open("./maps/1.txt", "r")
        lines = file.readlines()
        file.close()
        self.tiles = []
        for i in range(len(lines)):
            tile = lines[i].split(" ")
            self.tiles.append(Tile((int(tile[0]), int(tile[1])), int(tile[2]), int(tile[3])))
        
        self.image = pygame.image.load("./resources/images/background2.png").convert()
    
    def render(self, window):
        #window.blit(self.image, (0, 0))
        for i in self.tiles:
            i.render(window)
    
    def getTileAt(self, pos):
        matching_tiles = []
        for i in self.tiles:
            if i.pos == pos:
                matching_tiles.append(i)
        if matching_tiles == []:
            return False
        else:
            return matching_tiles