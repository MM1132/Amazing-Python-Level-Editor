import pygame
from TileType import TILES
class Inventory:
    def __init__(self):
        # surface is the dark transparent background of the inventory
        self.surface = pygame.Surface((1920, 1080))
        self.surface.set_alpha(200)
        # Weather the invenroy is currenty open or not
        self.open = False
        # The tile that is currenty selected
        self.selection = [0, 0]

    # This static function draws a box :D
    def drawBox(window, color, pos, lineWidth):
        pygame.draw.rect(window, color, (pos[0], pos[1], pos[2], lineWidth))
        pygame.draw.rect(window, color, (pos[0]+pos[2]-lineWidth, pos[1]+lineWidth, lineWidth, pos[3]-lineWidth))
        pygame.draw.rect(window, color, (pos[0], pos[1]+lineWidth, lineWidth, pos[3]-lineWidth))
        pygame.draw.rect(window, color, (pos[0]+lineWidth, pos[1]+pos[3]-lineWidth, pos[2]-lineWidth*2, lineWidth))

    # Render all the renderable things of the inventory
    def render(self, window):
        window.blit(self.surface, (0, 0))

        # Draw a box around the tile that is currently selected
        Inventory.drawBox(window, (0, 0, 255), (100+self.selection[1]*150-5, 100+self.selection[0]*150-5, 110, 110), 5)

        for i in range(len(TILES)):
            for j in range(len(TILES[i])):
                window.blit(pygame.transform.scale(TILES[i][j], (100, 100)), (100+j*150, 100+i*150))
                if pygame.mouse.get_pos()[0] > 100+j*150 and pygame.mouse.get_pos()[0] < 200+j*150:
                    if pygame.mouse.get_pos()[1] > 100+i*150 and pygame.mouse.get_pos()[1] < 200+i*150:
                        Inventory.drawBox(window, (255, 0, 0), (100+j*150-5, 100+i*150-5, 110, 110), 5)

    # If mouse is over a tile, select that tile :D
    def changeSelection(self):
        for i in range(len(TILES)):
            for j in range(len(TILES[i])):
                if pygame.mouse.get_pos()[0] > 100+j*150 and pygame.mouse.get_pos()[0] < 200+j*150:
                    if pygame.mouse.get_pos()[1] > 100+i*150 and pygame.mouse.get_pos()[1] < 200+i*150:
                        self.selection = [i, j]