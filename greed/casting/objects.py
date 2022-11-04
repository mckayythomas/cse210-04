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
        if self._move_counter < 2:
            self._move_counter += 1
        else:
            self._position.y += 1
            self._move_counter = 0

    def create_objects(self, cast, COLS, ROWS):
        DEFAULT_ARTIFACTS = random.randint(3, 8)
        for n in range(DEFAULT_ARTIFACTS):

            x = random.randint(1, 60 - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(15)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            # create the Gems
            gems = Objects()
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            gems.set_text("*")
            gems.set_font_size(15)
            gems.set_color(color)
            gems.set_position(position)
            cast.add_actor("gems", gems)

            # create the Rocks
            stones = Objects()
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            stones.set_text("o")
            stones.set_color(color)
            stones.set_font_size(15)
            stones.set_position(position)
            cast.add_actor("stones", stones)
