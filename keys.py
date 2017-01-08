import components
import settings
from bearlibterminal import terminal

def handle_keys(world, entity):
    key = terminal.read()
    if key == terminal.TK_ESCAPE:
        return 'exit'
    elif key == terminal.TK_UP:
        world.component_for_entity(entity, components.Movement).y = -1
    elif key == terminal.TK_DOWN:
        world.component_for_entity(entity, components.Movement).y = 1
    elif key == terminal.TK_LEFT:
        world.component_for_entity(entity, components.Movement).x = -1
    elif key == terminal.TK_RIGHT:
        world.component_for_entity(entity, components.Movement).x = 1
