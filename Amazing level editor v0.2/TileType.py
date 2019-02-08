import pygame

# The amazing function for loading in all the tiles
def getTexture(file, size, alpha, resourcepack):
    image = pygame.image.load("./resourcepacks/" + resourcepack + "/tiles/" + file + ".png").convert()
    part = []
    for i in range(int(image.get_width() / size)):
        rect = pygame.Rect(i * size, 0, size, size)
        texture = pygame.Surface(rect.size)
        texture.blit(image, (0, 0), rect)
        texture.set_colorkey(alpha)
        part.append(texture)
    return part

TILES = []
# Lets load all the tiles in and save the into the TILES variable :D
with open("./config.cfg") as f:
    for i in f:
        if i.split("=")[0] == "resourcepack":
            for j in ["dirt", "stone"]:
                TILES.append(getTexture(j, 50, (0, 38, 255, 255), i.split("=")[1]))