import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

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
        
        player_1 = cast.get_first_actor("snakes")
        player_1.turn_head(self._direction)

class ControlActorsAction_Player2(ControlActorsAction):
    '''
    This is a child function of ControlActorsAction. It is designed to demonstrate 
    polymorphism and inheritance
    '''

    def execute(self, cast, script):
        """Executes the control actors action for player 2.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        #If you want to alter keybindings for player 2 alter these variables
        _move_left = 'j'
        _move_right = 'l'
        _move_up = 'i'
        _move_down = 'k'


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
        
        player_2 = cast.get_first_actor("snakes2")
        player_2.turn_head(self._direction)


        