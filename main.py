import esper
from bearlibterminal import terminal
import settings
import keys
import processors
import components


def make_map(world):
    for x in range(settings.MAP_WIDTH):
        for y in range(settings.MAP_HEIGHT):
            world.create_entity(
                components.Position(x, y),
                components.BlocksMovement(),
                components.BlocksSight(),
                components.Render(14, 1)
            )


def run():
    terminal.open()
    terminal.set("""window: title='Roguelike',
                            size={0}x{1};
                    font:   {2},
                            size=16x16"""
                 .format(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, settings.FONT))

    world = esper.World()
    player = world.create_entity()
    world.add_component(player, components.Movement())
    world.add_component(player, components.Position(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
    world.add_component(player, components.Render(17, 2))
    world.add_component(player, components.BlocksMovement())
    world.add_component(player, components.Health(50))
    world.add_component(player, components.PlayerControlled())

    make_map(world)

    render_processor = processors.RenderProcessor()
    movement_processor = processors.MovementProcessor()
    world.add_processor(render_processor, priority=1)
    world.add_processor(movement_processor, priority=2)

    while True:
        if keys.handle_keys(world, player) == 'exit':
            break
        world.process()

    terminal.close()

if __name__ == "__main__":
    run()
