from game.casting.cast import Cast
from game.casting.space import Space
from game.casting.score import Score
from game.casting.spaceship import Spaceship
from game.casting.bullets import Bullets

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

def main():
    
    cast = Cast()

    cast.add_actor("space", Space())

    cast.add_actor("score", Score(1))
    cast.add_actor("score", Score(2))

    cast.add_actor("spaceship", Spaceship(1))
    cast.add_actor("spaceship", Spaceship(2))

    cast.add_actor("bullets", Bullets(1))
    cast.add_actor("bullets", Bullets(2))
    
    keyboard_service = KeyboardService()
    video_service = VideoService()
    
    script = Script()
    
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()