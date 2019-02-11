import pygame

# The amazing function for loading in all the tiles
def getTexture(tile, size, alpha, resourcepack):
    image = pygame.image.load("./resourcepacks/" + resourcepack + "/tiles/" + tile[0] + ".png").convert()
    part = []
    for i in range(int(image.get_width() / size)):
        rect = pygame.Rect(i * size, 0, size, size)
        texture = pygame.Surface(rect.size)
        texture.blit(image, (0, 0), rect)
        texture.set_colorkey(alpha)
        part.append(texture)
    return [part, tile[1]]

DIRT = None
STONE = None
LADDER = None
# Basically just get the name of the active resource pack that should be loaded
with open("./resourcepacks/resourcepack.cfg", "r") as f:
    # Get all the settings for the resourcepack from the config file
    settings = [i.strip().split("=") for i in f]
    for i in range(len(settings)):
        if settings[i][0] == "resourcepack":
            pack = settings[i][1]

# Open the tiles config file
with open("./resourcepacks/" + pack + "/tiles.cfg") as f:
    # Read all the files lines
    fileLines = [i.strip() for i in f]
    # Loop through the files lines
    for i in fileLines:
        # Split the information at the line
        info = i.split("=")
        # If the line is about dirt
        if info[0] == "dirt":
            # Load in all dirts textures and append them to dirt
            DIRT = getTexture(eval(info[1]), 50, (0, 38, 255), pack)
        # But if the info is about stone
        elif info[0] == "stone":
            # Load in all stones textures and append them to stone
            STONE = getTexture(eval(info[1]), 50, (0, 38, 255), pack)
        # But if the info is about ladder
        elif info[0] == "ladder":
            # Load in all the ladders textures and append them to ladder texture list
            LADDER = getTexture(eval(info[1]), 50, (0, 38, 255), pack)