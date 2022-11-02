from .player import Player


class Objects(Player):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""

    def rock_gem(self):
        return self._point
    
    def get_item_type(self):
        return self._object
