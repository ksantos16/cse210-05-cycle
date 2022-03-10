import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.move_actors_action import MoveActorsAction


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snakes collides
    with each other's segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._loser = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        segments = []

        for snake in snakes:
            segments += snake.get_segments()[1:]

        for snake in snakes:
            head = snake.get_segments()[0]
            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    self._is_game_over = True
                    self._loser = snakes.index(snake)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            if self._loser == 0:
                notification = "Player 1 lost! "
            else:
                notification = "Player 2 lost! "

            snakes = cast.get_actors("snakes")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            final_message = notification + "Game Over!"

            message = Actor()
            message.set_text(final_message)
            message.set_position(position)
            cast.add_actor("messages", message)

            for snake in snakes:
                snake._color = constants.WHITE
                segments = snake.get_segments()

                for segment in segments:
                    segment.set_color(constants.WHITE)
