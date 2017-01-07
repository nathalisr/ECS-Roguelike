class Input:
    def __init__(self):
        print("teste")


class Health:
    def __init__(self, hp):
        self.hp = hp


class PlayerControlled: #precisa criar um processor que faz: for each playerControlled entity: do something
    pass


class BlocksMovement:
    pass


class BlocksSight:
    pass


class Position:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy


class Render:
    def __init__(self, tile, layer):
        self.tile = tile
        self.layer = layer


class Movement:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
