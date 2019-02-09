import pygame
TILE = [[], [], []]

dirt = pygame.image.load("./resources/images/dirt6.png")
stone = pygame.image.load("./resources/images/stone.png")
ladder = pygame.image.load("./resources/images/ladder1.png")
alpha = dirt.get_at((101, 1))
for i in range(9):
    rect = pygame.Rect(i * 50, 0, 50, 50)
    image = pygame.Surface(rect.size)
    image.blit(dirt, (0, 0), rect)
    image.set_colorkey(alpha)
    TILE[0].append(image)
for i in range(4):
    rect = pygame.Rect(i * 50, 0, 50, 50)
    image = pygame.Surface(rect.size)
    image.blit(stone, (0, 0), rect)
    image.set_colorkey(alpha)
    TILE[1].append(image)
for i in range(1):
    rect = pygame.Rect(i * 50, 0, 50, 50)
    image = pygame.Surface(rect.size)
    image.blit(ladder, (0, 0), rect)
    image.set_colorkey(alpha)
    TILE[2].append(image)
del dirt, stone, ladder, alpha

"""
self.tiles = []
    for i in range(13):
        rect = pygame.Rect(i * 22, 0, 22, 22)
        image = pygame.Surface(rect.size).convert()
        image.blit(sheet, (0, 0), rect)
        alpha = image.get_at((0, 0))
        image.set_colorkey(alpha)
        self.tiles.append(pygame.transform.scale(image, (88, 88)))
"""