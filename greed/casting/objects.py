import random
from .actor import Actor
from ..shared.point import Point
from ..shared.color import Color


class Objects(Actor):
    """
    An item of cultural or historical interest. 

    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """

    def __init__(self):
        super().__init__()
        self._message = ""
        self._move_counter = 0
        self._velocity = Point(0, 0)

    def rock_gem(self):
        return self._point

    def get_item_type(self):
        return self._object

    def fall(self):
        if self._move_counter < 10:
            self._move_counter += 1
        else:
            self._position.y += 5
            self._move_counter = 0

    def create_objects(self, cast, COLS, ROWS, CELL_SIZE=15):
        DEFAULT_ARTIFACTS = random.randint(2, 5)
        for n in range(DEFAULT_ARTIFACTS):

            y = 0

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            # create the Gems
            gems = Objects()
            x1 = random.randint(1, COLS - 1)
            position = Point(x1, y)
            position = position.scale(CELL_SIZE)
            gems.set_text("*")
            gems.set_font_size(15)
            gems.set_color(color)
            gems.set_position(position)
            cast.add_actor("gems", gems)

            # create the Rocks
            stones = Objects()
            x2 = x1
            while x2 == x1:
                x2 = random.randint(1, COLS - 1)
            position = Point(x2, y)
            position = position.scale(CELL_SIZE)
            stones.set_text("o")
            stones.set_color(color)
            stones.set_font_size(15)
            stones.set_position(position)
            cast.add_actor("stones", stones)
