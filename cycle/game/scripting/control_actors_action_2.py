import constants
from game.scripting.action import Action
from game.scripting.control_actors_action import ControlActorsAction
from game.shared.point import Point


class ControlActorsAction_2(ControlActorsAction):
    # Polymophism from ControlActorsAction
    # Override the execute(cast, script) method as follows:

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._move_left = 'j'
        self._move_right = 'l'
        self._move_up = 'i'
        self._move_down = 'k'
        self._player_number = 1