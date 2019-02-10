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
menu = Menu()
map = None
inventory = Inventory()

# This will be running only when menu_state is active
def menu_state():
    event = menu.getInput()
    if event == "quit": return False
    elif type(event) == str and event[-4:] == ".map":
        return event
    menu.render(window)

# This will be running only when game_state is active
def game_state():
    event = input.get_event()
    if event == "quit": return False
    elif event == "back": return "back"
    elif event == 1:
        if inventory.open:
            inventory.changeSelection()
        else:
            map.placeTile(inventory.selection)
    elif event == 3:
        if not inventory.open:
            map.removeTile()
    elif event == "space":
        map.offset = [35, 15]
    elif event == "invOpen":
        inventory.open = True
    elif event == "invClosed":
        inventory.open = False
    window.fill((255, 255, 255))

    map.update(input.middle)
    map.render(window)

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
        map = Map(event)
        menu = None
    elif event == "back":
        state = menu_state
        map.save()
        map = None
        menu = Menu()

    pygame.display.update()
pygame.quit()