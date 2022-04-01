from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        space = cast.get_actor("space", 0)
        score1 = cast.get_actor("score", 0)
        score2 = cast.get_actor("score", 1)
        ship1 = cast.get_actor("spaceship", 0)
        ship2 = cast.get_actor("spaceship", 1)

        bulletObj1 = cast.get_actor("bullets", 0)
        bullets1 = bulletObj1.get_bullets()

        bulletObj2 = cast.get_actor("bullets", 1)
        bullets2 = bulletObj2.get_bullets()
        
        messages = cast.get_actor("messages", 0)
        
        self._video_service.draw_space(space)
        self._video_service.draw_border()
        self._video_service.draw_bullets(bullets1)
        self._video_service.draw_bullets(bullets2)
        self._video_service.draw_ship(ship1)
        self._video_service.draw_ship(ship2)
        self._video_service.draw_score(score1)
        self._video_service.draw_score(score2)
        if messages != None:
            self._video_service.draw_winner(messages)