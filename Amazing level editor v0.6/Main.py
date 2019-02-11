import pygame
pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Amazing Level Editor")

# Need to import all the classes after the creation of the games display
from Input import Input
from Menu import Menu
from Map import Map
from Inventory import Inventory

# Create objects for the classes
input = Input()
activeObject = Menu()
inventory = Inventory()

# This will be running only when menu_state is active
def menu_state():
    event = activeObject.getInput()
    if event == "quit": return False
    elif type(event) == str and event[-4:] == ".map":
        return event
    activeObject.render(window)

# This will be running only when game_state is active
def game_state():
    event = input.get_event()
    if event == "quit": return False
    elif event == "back": return "back"
    elif input.leftClick:
        if inventory.open:
            inventory.changeSelection()
        else:
            activeObject.placeTile(inventory.selection)
    elif input.rightClick:
        if not inventory.open:
            activeObject.removeTile()
    elif event == "space":
        activeObject.centerCamera()
    elif event == "invOpen":
        inventory.open = True
    elif event == "invClosed":
        inventory.open = False
    window.fill((255, 255, 255))

    activeObject.update(input.middle)
    activeObject.render(window)

    if inventory.open:
        inventory.render(window)

# Some general variables :D
state = menu_state
running = True

# The main loop of the game
while running:
    event = state()
    if event == False: running = False
    elif type(event) == str and event[-4:] == ".map":
        state = game_state
        activeObject = Map(event)
    elif event == "back":
        state = menu_state
        activeObject.save()
        activeObject = Menu()

    pygame.display.update()
pygame.quit()