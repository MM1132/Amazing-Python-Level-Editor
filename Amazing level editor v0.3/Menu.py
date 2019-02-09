import pygame
from Button import Button
from FileBrowser import FileBrowser
class Menu:
    def __init__(self):
        # The current state and the background of the menu
        self.state = 0
        self.background = pygame.image.load("./resources/images/forest.png").convert()

        # Configure manu's elements (buttons, file browers, etc..)
        self.elements = {
            0: [Button("Create new", 2, ["centered", 300]), Button("Load level", 1, ["centered", 400]), Button("Exit", "quit", ["centered", 500])],
            1: [FileBrowser("./saves/", ".map", ["centered", 200]), Button("Back", 0, ["centered", 800])],
            2: [Button("Back", 0, ["centered", 800])]
        }

    # Render all of menu
    def render(self, window):
        window.blit(self.background, (0, 0))
        for i in self.elements[self.state]:
            i.render(window)

    # Get input from the user and do stuff according to it
    def getInput(self):
        for event in pygame.event.get():
            # ALL OF QUITTING CODE
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"

            # HANDLE PRESSES OF THE BUTTONS
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in self.elements[self.state]:
                        if type(i) == Button:
                            if i.hover:
                                if type(i.returnValue) == int:
                                    self.state = i.returnValue
                                elif type(i.returnValue) == str:
                                    return i.returnValue
                        elif type(i) == FileBrowser:
                            for j in i.elements:
                                if j.hover:
                                    if type(j) == Button:
                                        return j.returnValue