import pygame, os
import Input, Map, Player
pygame.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"
window = pygame.display.set_mode((1400, 1000))
pygame.display.set_caption("Adventure Game")

input = Input.Input()
map = Map.Map()
player = Player.Player(map)

clock = pygame.time.Clock()

running = True
def game():
    global running
    event = input.getInput()
    if event == "quit": running = False
    
    player.update(input.activeKeys)
    
    map.render(window)
    player.render(window)

game_state = game
while running:
    window.fill((255, 255, 255))
    clock.tick(60)
    game_state()
    pygame.display.update()
pygame.quit()