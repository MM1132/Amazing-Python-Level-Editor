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
        # Inventory.drawBox(window, (0, 0, 255), (85+self.selection[1]*150-5, 85+self.selection[0]*150-5, 110, 110), 5)

        position = [0, 0]
        for i in range(len(TILES)):
            for j in range(len(TILES[i])):
                # Draw the tiles texture
                window.blit(pygame.transform.scale(TILES[i][j], (100, 100)), (85 + position[0] * 150, 85 + position[1] * 150))
                # Draw box around selection
                if self.selection == [i, j]:
                    Inventory.drawBox(window, (0, 0, 255), (85+position[0]*150-5, 85+position[1]*150-5, 110, 110), 5)

                # Draw the mouseOver effect box to tiles
                mouse = pygame.mouse.get_pos()
                if mouse[0] > 85 + position[0] * 150 and mouse[0] < 85 + 100 + position[0] * 150:
                    if mouse[1] > 85 + position[1] * 150 and mouse[1] < 85 + 100 + position[1] * 150:
                        Inventory.drawBox(window, (255, 0, 0), (85 + position[0] * 150-5, 85 + position[1] * 150-5, 110, 110), 5)

                # Update the position of the render so we can move to the next tile and render that on the next run of the loop
                position[0] += 1
                if position[0] > 11: position[0] = 0; position[1] += 1

    # If mouse is over a tile, select that tile in the inventory :D
    def changeSelection(self):
        position = [0, 0]
        mouse = pygame.mouse.get_pos()
        for i in range(len(TILES)):
            for j in range(len(TILES[i])):
                if mouse[0] > 85 + position[0] * 150 and mouse[0] < 85 + 100 + position[0] * 150:
                    if mouse[1] > 85 + position[1] * 150 and mouse[1] < 85 + 100 + position[1] * 150:
                        self.selection = [i, j]
                position[0] += 1
                if position[0] > 11: position[0] = 0; position[1] += 1