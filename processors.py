import esper
from bearlibterminal import terminal
import components


class InputProcessor:
    def __init__(self):
        super().__init__()


class RenderProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        terminal.clear()
        for entity, (render, position) in self.world.get_components(components.Render, components.Position):
            terminal.layer(render.layer)
            terminal.put(position.x, position.y, render.tile)
        terminal.refresh()


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for entity, (position, movement) in self.world.get_components(components.Position, components.Movement):
            position.x += movement.x
            position.y += movement.y
            # reset the direction of movement so they don't keep moving in that direction every turn.
            movement.x = 0
            movement.y = 0
