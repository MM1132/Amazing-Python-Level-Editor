import pygame

class TextBox:
    def __init__(self, size, pos):
        self.pos = pos
        self.color = (100, 255, 50)

        self.text = ""

        self.font = pygame.font.SysFont("Verdana", size)
        self.fontRender = self.font.render(self.text, 1, self.color)

        if self.pos[0] == "centered":
            self.centeredX = True
        else:
            self.centeredX = False

    def render(self, window):
        # Update the text in the textbox
        self.fontRender = self.font.render(self.text, 1, self.color)
        # Update the textboxes psoition to be in the center
        if self.centeredX:
            self.pos[0] = 1920 / 2 - self.fontRender.get_width() / 2
        # Draw the fucking text in the textbox
        window.blit(self.fontRender, self.pos)
        # Finally draw box around the text :D
        pygame.draw.rect(window, (0, 0, 0), (self.pos[0], self.pos[1], self.fontRender.get_width(), self.fontRender.get_height()), 5)

    def update(self, event):
        # If the key is backspace, delete the last character of the text
        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        # If enter key is pressed: create the level
        elif event.key == pygame.K_RETURN:
            return True
        # Else, just add the shit to the text
        else:
            self.text += event.unicode