from ..shared.color import Color
from ..casting.objects import Objects
from ..shared.point import Point

class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        templist = []

        for group in self._actors:
            #Check actors position to see if they have reached the end of the y axis and remove items off page
            if(group == "gems" or  group=="stones"):
                templist.extend(self._actors[group])
                for item in templist:
                    p = item.get_position()
                    y = p.get_y()
                    if y > 600:
                        self.remove_actor(self, item)
            results.extend(self._actors[group])


        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group but only returns player or score.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if(group == 'score'):
            if group in self._actors.keys():
                result = self._actors[group][0]
        elif(group == 'player'):
            if group in self._actors.keys():
                result = self._actors[group][0]
        return result

    def remove_actor(self, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        '''If actor group is gem or stone'''
        if((actor.group == "gem") or (actor.group == "stone")):
            p = actor.position.get_position()
            y = p.get_y()
            if y < 600:
                '''Create a blank Object to replace it if not at the end of the screen'''
                blank_object = Objects()
                blank_object.set_text(chr(' '))
                blank_object.set_font_size(15)
                blank_object.set_color(Color(0, 0, 0))
                blank_object.set_position(actor.position)
                self.add_actor("blank", blank_object)
                self._actors[actor.group].add(blank_object)
            '''Then delete the initial object'''
            self._actors[actor.group].remove(actor)
