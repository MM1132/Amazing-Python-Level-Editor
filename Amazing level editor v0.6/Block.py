from Tile import Tile

class Block(Tile):
    def __init__(self, pos, texture):
        self.pos = pos
        self.texture = texture
        self.renderPos = [pos[0] * 50, pos[1] * 50]