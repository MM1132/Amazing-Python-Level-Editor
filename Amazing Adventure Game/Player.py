import pygame
class Player:
    def __init__(self, map):
        self.map = map
        self.pos = [120, 50]
        self.speed = 4
        
        self.fallingSpeed = 6
        
        # 0 = stand
        # 1 = running_right
        # 2 = running_left
        # 3 = falling
        # 4 = ladder_up
        # 5 = ladder_down
        # 6 = ladder_standing
        # 7 = jump_right
        # 8 = jump_left
        self.state = 3
        
        self.jumpPos = None
        
        self.animationFrame = 0
        self.running = []
        image = pygame.image.load("./resources/images/running.png").convert()
        alpha = image.get_at((0, 0))
        for i in range(8):
            rect = pygame.Rect(i * 32, 0, 32, 32)
            piece = pygame.Surface(rect.size).convert()
            piece.blit(image, (0, 0), rect)
            piece.set_colorkey(alpha)
            piece = pygame.transform.scale(piece, (55, 55))
            self.running.append(piece)
        del image, alpha
    
    def update(self, activeKeys):
        # Save all the five tiles that are near the player
        #up, down, right, left, middle
        nearTiles = []
        middle = ((self.pos[0] + 25) // 50, (self.pos[1] + 25) // 50)
        nearTiles.append(self.map.getTileAt((middle[0], middle[1] - 1)))
        nearTiles.append(self.map.getTileAt((middle[0], middle[1] + 1)))
        nearTiles.append(self.map.getTileAt((middle[0] + 1, middle[1])))
        nearTiles.append(self.map.getTileAt((middle[0] - 1, middle[1])))
        nearTiles.append(self.map.getTileAt(middle))
        
        # FALLING
        if self.state == 3:
            # Move the player down a little
            self.pos[1] += self.fallingSpeed
            # If we have a tile under us
            if nearTiles[1] != False:
                # If the nearTiles bottom list contains a tile with good type
                if any(i.type == 0 for i in nearTiles[1]) or any(i.type == 1 for i in nearTiles[1]) or any(i.type == 2 for i in nearTiles[1]):
                    # Stop falling at the tile and set the state to standing
                    if self.pos[1] + 50 > nearTiles[1][0].blitPos[1]: # Always stop at the first tile in the list
                        self.pos[1] = nearTiles[1][0].blitPos[1] - 50
                        self.state = 0
                        self.animationFrame = 0
        # STANDING
        elif self.state == 0:
            # If press up
            if activeKeys[0]:
                # If the players middle coordinate is not empty
                if nearTiles[4] != False:
                    # If the players middle coordinate contains a tile of ladder
                    if any(i.type == 2 for i in nearTiles[4]):
                        # Ladder_up
                        self.state = 4
                        self.animationFrame = 0
            # If press down
            elif activeKeys[1]:
                # If the bottom tile is not empty
                if nearTiles[1] != False:
                    # If the bottom tile list contains a ladder
                    if any(i.type == 2 for i in nearTiles[1]):
                        # Ladder_down
                        self.state = 5
                        self.animationFrame = 0
            # If press right
            elif activeKeys[2]:
                # Running_right
                self.state = 1
                self.animationFrame = 0
            # If press left
            elif activeKeys[3]:
                # Running_left
                self.state = 2
                self.animationFrame = 0
        # RUNNING LEFT
        elif self.state == 2:
            # If holding down left arrow
            if activeKeys[3]:
                # If we have some kind of block under ourselves
                if nearTiles[1] != False:
                    # If there is nothing blocking the player on the left (tile contains either nothing or a ladder)
                    if nearTiles[3] == False or any(i.type == 2 for i in nearTiles[3]):
                        # Run to the left
                        self.pos[0] -= self.speed
                    # If the tile on the left is either dirt of stone
                    elif any(i.type == 0 for i in nearTiles[3]) or any(i.type == 1 for i in nearTiles[3]):
                        # If the player is not inside the wall yet
                        if self.pos[0] - 50 > nearTiles[3][0].blitPos[0]:
                            # Move the player little to the right
                            self.pos[0] -= self.speed
                        elif self.pos[0] - 50 < nearTiles[3][0].blitPos[0] and self.pos[0] - 50 > nearTiles[3][0].blitPos[0] - self.speed:
                            # Keep the player form moving into the wall
                            self.pos[0] = nearTiles[3][0].blitPos[0] + 50
                            # Set the state of player to standing
                            self.state = 0
                            self.animationFrame = 0
                # If we do not have a block under ourselves
                elif nearTiles[1] == False:
                    # Change state to falling
                    self.state = 3
                    self.animationFrame = 0
            # If the right arrow is down instead
            elif activeKeys[2]:
                # Change state to running to the right
                self.state = 1
            # If we press up arrow while running to the left
            elif activeKeys[0]:
                # If we have a tile in the middle
                if nearTiles[4] != False:
                    # And if that tile is a ladder type of a tile
                    if any(i.type == 2 for i in nearTiles[4]):
                        # Then change the state to ladder_up
                        self.state = 4
                        self.animationFrame = 0
            # If we press down arrow while running to the left
            elif activeKeys[1]:
                # If we have a tile below ourselves
                if nearTiles[1] != False:
                    # And if that tile is a ladder
                    if any(i.type == 2 for i in nearTiles[1]):
                        # Change the state to ladder_down
                        self.state = 5
                        self.animationFrame = 0
            # But if no keys are down
            elif activeKeys == [False, False, False, False]:
                # Change the state to standing
                self.state = 0
                self.animationFrame = 0
        # RUNNING RIGHT
        elif self.state == 1:
            # If holding down right arrow
            if activeKeys[2]:
                # if we have block under:
                if nearTiles[1] != False:
                    # If there is nothing blocking us on the right
                    if nearTiles[2] == False or any(i.type == 2 for i in nearTiles[2]):
                        # Run to the right
                        self.pos[0] += self.speed
                    # If the tile of the right side is either dirt or stone
                    elif any(i.type == 0 for i in nearTiles[2]) or any(i.type == 1 for i in nearTiles[2]):
                        # If the player is not inside the wall yet
                        if self.pos[0] + 50 < nearTiles[2][0].blitPos[0]:
                            # Move the player little to the right
                            self.pos[0] += self.speed
                        elif self.pos[0] + 50 > nearTiles[2][0].blitPos[0] and self.pos[0] + 50 < nearTiles[2][0].blitPos[0] + self.speed:
                            # Keep the player form moving into the wall
                            self.pos[0] = nearTiles[2][0].blitPos[0] - 50
                            # Set the state of player to standing
                            self.state = 0
                            self.animationFrame = 0
                # If we don't have any tile under ourselves
                elif nearTiles[1] == False:
                    # Change the state to falling
                    self.state = 3
                    self.animationFrame = 0
            # If the left arrow key is down instead
            elif activeKeys[3]:
                # Change the state to running to the left
                self.state = 2
            # If the up arrow is pressed while running to the right
            elif activeKeys[0]:
                # If we have a tile inside of us
                if nearTiles[4] != False:
                    # If that tile is a ladder
                    if any(i.type == 2 for i in nearTiles[4]):
                        # Change the state to ladder_up
                        self.state = 4
                        self.animationFrame = 0
            # If the down arrow is pressed while running right
            elif activeKeys[1]:
                # If we have a tile below ourselves
                if nearTiles[1] != False:
                    # If that tile is a ladder
                    if any(i.type == 2 for i in nearTiles[1]):
                        # Change the state to ladder_down
                        self.state = 5
                        self.animationFrame = 0
            # But if not arrows are pressed down what so ever
            elif activeKeys == [False, False, False, False]:
                # Change the state to standing
                self.state = 0
                self.animationFrame = 0
        # LADDER_UP
        elif self.state == 4:
            # If the up arrow is being pressed still
            if activeKeys[0]:
                # If we have a tile under ourselves
                if nearTiles[4] != False:
                    # If that tile contains a ladder type
                    if any(i.type == 2 for i in nearTiles[4]):
                        # Make the player centered to that ladder
                        self.pos[0] = nearTiles[4][0].blitPos[0]
                        # Move the player down
                        self.pos[1] -= self.speed
                # But if we have a tile below us
                elif nearTiles[1] != False:
                    # And that tile happens to contain a ladder
                    if any(i.type == 2 for i in nearTiles[1]):
                        # If we have not reached the top of the ladder yet
                        if self.pos[1] + 50 > nearTiles[1][0].blitPos[1]:
                            # Make the player centered to that ladder
                            self.pos[0] = nearTiles[1][0].blitPos[0]
                            # Move the player down
                            self.pos[1] -= self.speed
                        # If we have reached the top of the ladder
                        else:
                            # Set the Y of the player to the ground level
                            self.pos[1] = nearTiles[1][0].blitPos[1] - 50
                            # Change the state to standing
                            self.state = 0
                            self.animationFrame = 0
            # If DOWN, ladder_down, but only if there is a ladder below the player
            elif activeKeys[1]:
                if nearTiles[4] == False or any(i.type == 2 for i in nearTiles[4]):
                    self.state = 5
            # If the right arrow is pressed while on the ladder
            elif activeKeys[2]:
                # if there is no block on the way on the right side
                if nearTiles[2] == False or nearTiles[2][0].type == 2:
                    # Start the jump to the right
                    self.state = 7
                    self.animationFrame = 0
                    # Set the position to jump to
                    self.jumpPos = self.pos[0] + 50
            # If the left key is pressed while on the ladder
            elif activeKeys[3]:
                # If there is not block on the way on the left side
                if nearTiles[3] == False or nearTiles[3][0].type == 2:
                    # Start jumping to the left
                    self.state = 8
                    self.animationFrame = 0
                    # Set the position to jump to
                    self.jumpPos = self.pos[0] - 50
        # LADDER_DOWN
        elif self.state == 5:
            # If up arrow is being pressed:
            if activeKeys[0]:
                # Change the state to ladder_up
                self.state = 4
            # If pressing down
            elif activeKeys[1]:
                # If there is ladder in middle or under
                if nearTiles[1] != False and any(i.type == 2 for i in nearTiles[1]):
                    self.pos[1] += self.speed
                    self.pos[0] = nearTiles[1][0].blitPos[0]
                elif nearTiles[4] != False and any(i.type == 2 for i in nearTiles[4]):
                    self.pos[1] += self.speed
                    self.pos[0] = nearTiles[4][0].blitPos[0]
                    if nearTiles[1] != False and (nearTiles[1][0].type == 0 or nearTiles[1][0].type == 1):
                        if self.pos[1] > nearTiles[4][0].blitPos[1]:
                            self.pos[1] = nearTiles[4][0].blitPos[1]
                            self.state = 0
                else:
                    self.state = 3
            # If the right arrow is pressed while on the ladder
            elif activeKeys[2]:
                # if there is no block on the way on the right side
                if nearTiles[2] == False or nearTiles[2][0].type == 2:
                    # Start the jump to the right
                    self.state = 7
                    self.animationFrame = 0
                    # Set the position to jump to
                    self.jumpPos = self.pos[0] + 50
            # If the left key is pressed while on the ladder
            elif activeKeys[3]:
                # If there is not block on the way on the left side
                if nearTiles[3] == False or nearTiles[3][0].type == 2:
                    # Start jumping to the left
                    self.state = 8
                    self.animationFrame = 0
                    # Set the position to jump to
                    self.jumpPos = self.pos[0] - 50
                    
        # JUMP_RIGHT
        elif self.state == 7:
            self.pos[0] += self.speed
            if self.pos[0] > self.jumpPos:
                self.pos[0] = self.jumpPos
                self.state = 3
                self.animationFrame = 0
        # JUMP_LEFT
        elif self.state == 8:
            self.pos[0] -= self.speed
            if self.pos[0] < self.jumpPos:
                self.pos[0] = self.jumpPos
                self.state = 3
                self.animationFrame = 0
        print(self.animationFrame)
        
    def render(self, window):
        window.blit(self.running[0], (self.pos[0], self.pos[1]))