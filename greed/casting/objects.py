from .actor import Actor


class Objects(Actor):
    """
    A rock or gem
    
    The responsibility of an Object is to provide points depending if it is a rock or a gem.

    Attributes:
        self._point (Int) a set of points depending on if it is a rock or a gem

    """
    def __init__(self):
        super().__init__()
        self._point = 0

    def rock_gem(self, group):
        if group == "gems":
            self._point += 100
        elif group == "stones":
            self._point -= 100

        return self._point
    
    def get_item_type(self):
        return self._object
