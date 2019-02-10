import pygame
class Button:
    # First initialization of the button
    def __init__(self, text, returnValue, pos):
        self.text = text
        self.returnValue = returnValue
        self.pos = pos
        self.color = (200, 50, 50)
        self.hoverColor = (0, 255, 0)
        self.hover = False
        
        self.font = pygame.font.SysFont("Arial", 40)
        self.fontRender = self.font.render(self.text, 1, self.color)

        # Weather the button is suppoed to be centered of not
        if type(pos[0]) == str and pos[0] == "centered":
            self.pos[0] = 1920 // 2 - self.fontRender.get_width() // 2

    # Render the button
    def render(self, window):
        mouse = pygame.mouse.get_pos()
        # If mouse is over the button, change buttons colour and buttons hover state
        if mouse[0] > self.pos[0] and mouse[1] > self.pos[1] and mouse[0] < self.pos[0] + self.fontRender.get_width() and mouse[1] < self.pos[1] + self.fontRender.get_height():
            self.fontRender = self.font.render(self.text, 1, self.hoverColor)
            self.hover = True
        else:
            self.fontRender = self.font.render(self.text, 1, self.color)
            self.hover = False
        # Draw the button onto the screen
        window.blit(self.fontRender, self.pos)