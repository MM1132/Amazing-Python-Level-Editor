import pygame
class Input:
    def __init__(self):
        self.activeKeys = [False, False, False, False]
    
    def getInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                if event.key == pygame.K_UP:
                    self.activeKeys =[True, False, False, False]
                elif event.key == pygame.K_DOWN:
                    self.activeKeys = [False, True, False, False]
                elif event.key == pygame.K_RIGHT:
                    self.activeKeys = [False, False, True, False]
                elif event.key == pygame.K_LEFT:
                    self.activeKeys = [False, False, False, True]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.activeKeys[0] = False
                elif event.key == pygame.K_DOWN:
                    self.activeKeys[1] = False
                elif event.key == pygame.K_RIGHT:
                    self.activeKeys[2] = False
                elif event.key == pygame.K_LEFT:
                    self.activeKeys[3] = False