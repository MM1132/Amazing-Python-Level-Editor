import pygame

class Input:
    def __init__(self):
        # Weather the middle mouse button is being pressed or not
        self.middle = False

        # If the left mouse button is being pressed or not
        self.leftClick = False

        # If the left mouse button is being pressed or not
        self.rightClick = False

    # Here we get all input from the user
    def get_event(self):
        for event in pygame.event.get():
            # QUIT
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                # Go back to menu
                if event.key == pygame.K_ESCAPE:
                    return "back"
                # Center the camera
                elif event.key == pygame.K_SPACE:
                    return "space"
                # Open inventory
                elif event.key == pygame.K_e:
                    return "invOpen"
            elif event.type == pygame.KEYUP:
                # Close inventory :(
                if event.key == pygame.K_e:
                    return "invClosed"
            # Mouse stuff...
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Left click
                if event.button == 1:
                    self.leftClick = True
                # Right click
                elif event.button == 3:
                    self.rightClick = True
                # Middle click
                elif event.button == 2:
                    self.middle = True
            # Middle mouse button up
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:
                    self.middle = False
                elif event.button == 1:
                    self.leftClick = False
                elif event.button == 3:
                    self.rightClick = False