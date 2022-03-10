import constants
from game.scripting.action import Action
from game.scripting.control_actors_action import ControlActorsAction
from game.shared.point import Point


class ControlActorsAction_2(ControlActorsAction):
    # Polymophism from ControlActorsAction
    # Override the execute(cast, script) method as follows:

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        snake = cast.get_actor("snakes", 1)
        snake.turn_head(self._direction)