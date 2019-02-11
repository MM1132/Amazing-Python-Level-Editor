import pygame
from Tile import Tile
from glob import glob
from Dirt import Dirt
from Stone import Stone

# Weather there is a tile at the specifiead coords or not...
def tileInPos(tiles, pos):
    for i in tiles:
        if i.tilePos == pos:
            return True
            break
    return False

# Return all the surrounding blocks of the given coords
def getSurroundingBlocks(tiles, pos):
    surroundingTiles = [False, False, False, False]
    for i in tiles:
        if i.tilePos[0] == pos[0] and i.tilePos[1] == (pos[1] - 1):
            surroundingTiles[0] = i
        if i.tilePos[0] == pos[0] and i.tilePos[1] == (pos[1] + 1):
            surroundingTiles[1] = i
        if i.tilePos[1] == pos[1] and i.tilePos[0] == (pos[0] + 1):
            surroundingTiles[2] = i
        if i.tilePos[1] == pos[1] and i.tilePos[0] == (pos[0] - 1):
            surroundingTiles[3] = i
    return surroundingTiles

# Calculate what texture a tile should use based on others tiles around it
def calculateTexture(surr):
    # FOUR
    if surr[0] and surr[1] and surr[2] and surr[3]:return 0
    # THREE
    elif surr[1] and surr[2] and surr[3]:return 14
    elif surr[0] and surr[1] and surr[3]:return 11
    elif surr[0] and surr[1] and surr[2]:return 10
    elif surr[0] and surr[2] and surr[3]:return 9
    # TWO --- DIAGONAL STUFF
    elif surr[0] and surr[2]:return 4
    elif surr[2] and surr[1]:return 6
    elif surr[1] and surr[3]:return 7
    elif surr[3] and surr[0]:return 5
    # TWO --- VERTICAL AND HORIZONTAL
    elif surr[0] and surr[1]:return 8
    elif surr[2] and surr[3]:return 1
    # ONE
    elif surr[0]:return 12
    elif surr[1]:return 15
    elif surr[2]:return 2
    elif surr[3]:return 3
    # SINGLE BLOCK
    else:return 13

class Map:
    # Jah jah jah...
    # Load in the whole map from the provided file
    def __init__(self, file):
        self.file = file

        # If the saveFile already exists
        if file in glob("./saves/*.map"):
            # Open the file for reading
            with open(self.file, "r") as f:
                # Store all the lines as lists of numbers
                info = [list(map(int, i.strip().split(" "))) for i in f]
            # Create an empty list for tiles
            self.blocks = []
            # If there is anything in info
            if info != []:
                # Loop through all the lines of info
                for i in info:
                    # If the tile is a dirt block
                    if i[2] == 0:
                        # Append dirt to the blocks variable
                        self.blocks.append(Dirt([i[0], i[1]]))
                    # If it is a stone block in the file
                    elif i[2] == 1:
                        # Add stone block to the blocks variable
                        self.blocks.append(Stone([i[0], i[1]]))

            del info
        # If the saveFile doesn't exist, create it (:
        else:
            with open(self.file, "w") as f:
                self.blocks = []

        # Calculate and set textures for all the blocks:
        for i in self.blocks:
            # Get surrdoundings of the current placeable tile
            surr = getSurroundingBlocks(self.blocks, i.tilePos)
            # Calculate the texture for the current block
            i.texture = calculateTexture(surr)

        self.size = [37, 20]
        self.offset = [(1920-(self.size[0] * 50))//2, (1080-(self.size[1] * 50))//2]
        self.centerOffset = list(self.offset)
        self.mouse = [0, 0]

    # Set the camera to center
    def centerCamera(self):
        self.offset = list(self.centerOffset)

    # Change the offset of the tiles if middle click gets pressed...
    def update(self, middle):
        if middle:
            if pygame.mouse.get_pos()[0] < self.mouse[0]:
                self.offset[0] -= abs(self.mouse[0]-pygame.mouse.get_pos()[0])
            if pygame.mouse.get_pos()[0] >= self.mouse[0]:
                self.offset[0] += abs(self.mouse[0]-pygame.mouse.get_pos()[0])
            if pygame.mouse.get_pos()[1] < self.mouse[1]:
                self.offset[1] -= abs(self.mouse[1]-pygame.mouse.get_pos()[1])
            if pygame.mouse.get_pos()[1] >= self.mouse[1]:
                self.offset[1] += abs(self.mouse[1]-pygame.mouse.get_pos()[1])
        self.mouse = pygame.mouse.get_pos()

    # Render out all the tiles using the render function from the Tile class
    def render(self, window):
        for i in self.blocks:
            i.render(window, self.offset)
        pygame.draw.rect(window, (0, 0, 0), (self.offset[0], self.offset[1], self.size[0] * 50, self.size[1] * 50), 2)

    # Place a tile into the fucking map
    def placeTile(self, selection):
        mouse = [(pygame.mouse.get_pos()[0] - self.offset[0]) // 50, (pygame.mouse.get_pos()[1] - self.offset[1]) // 50]
        # If the coords aren't outside of the maps area
        if mouse[0] > -1 and mouse[0] < self.size[0] and mouse[1] > -1 and mouse[1] < self.size[1]:
            # Remove the tile that was on the place of mouse
            if tileInPos(self.blocks, mouse):
                self.removeTile()

            # Get surrdoundings of the current placeable tile
            surr = getSurroundingBlocks(self.blocks, mouse)
            # Calculate the texture for the current tile
            sel = calculateTexture(surr)

            if selection == 0:
                # Append the tile into the list of tiles
                self.blocks.append(Dirt(mouse, sel))
            elif selection == 1:
                self.blocks.append(Stone(mouse, sel))

            # Loop through this tiles surroundings
            for i in surr:
                # If there is a surrounding for it
                if i:
                    # For surroundings for that tile too
                    surroundings = getSurroundingBlocks(self.blocks, i.tilePos)
                    # Calculate the texture for the tile
                    sel = calculateTexture(surroundings)
                    # Change the tiles texture
                    i.texture = sel

    # Remove a tile at mouses coordinates
    def removeTile(self):
        mouse = [(pygame.mouse.get_pos()[0] - self.offset[0]) // 50, (pygame.mouse.get_pos()[1] - self.offset[1]) // 50]

        # Loop through all the tiles
        for i in range(len(self.blocks)):

            # Find the tile under mouses coords
            if self.blocks[i].tilePos == mouse:

                # Delete the tile
                del self.blocks[i]

                # Get surrdoundings of the current deleteable tile
                surr = getSurroundingBlocks(self.blocks, mouse)
                # Loop through all the surrounding tiles
                for i in surr:
                    # Is the tile object exists
                    if i:
                        # Get the surroundings of the tile that's surrounding the deleteable tile
                        surroundings = getSurroundingBlocks(self.blocks, i.tilePos)
                        # Calculate the texture for the tile
                        sel = calculateTexture(surroundings)
                        # Change the tiles texture
                        i.texture = sel

                # Break out once the tile is deleted and tiles around it updated
                # No need to loop through anything else
                break

    # Save the map into the fuckin' file when it's closed
    def save(self):
        with open(self.file, "w") as f:
            for i in self.blocks:
                if type(i) == Dirt:
                    f.write(str(i.tilePos[0]) + " " + str(i.tilePos[1]) + " 0\n")
                elif type(i) == Stone:
                    f.write(str(i.tilePos[0]) + " " + str(i.tilePos[1]) + " 1\n")