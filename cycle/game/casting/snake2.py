import constants
from game.casting.actor import Actor
# from game.shared.point import Point
from game.casting.snake import Snake


class Snake2(Snake):

    """
    A long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body(head_symbol="@", color="")

    def get_segments(self):
        return self._segments

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            segment = Actor()
            segment.set_color(constants.RED)
            # self._segments.append(segment)

    def _prepare_body(self, head_symbol="@"):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH, head_symbol="@"):

            color = constants.RED if i == 0 else constants.RED
            segment = Actor()
            segment.set_color(color)
            self._segments.append(segment)
