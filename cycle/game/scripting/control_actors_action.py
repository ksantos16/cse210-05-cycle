import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the actor.
    
    The responsibility of ControlActorsAction is to get the direction and move the actor's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        #If you want to alter keybindings for player 1 alter these variables
        _move_left = 'a'
        _move_right = 'd'
        _move_up = 'w'
        _move_down = 's'

        # left
        if self._keyboard_service.is_key_down(_move_left):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down(_move_right):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down(_move_up):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down(_move_down):
            self._direction = Point(0, constants.CELL_SIZE)

        
        snake = cast.get_actor("snakes", 0)
        snake.turn_head(self._direction)
