import os
import random
from tkinter.tix import ROW
from turtle import *

from greed.casting.actor import Actor
from greed.shared.color import Color
from greed.shared.point import Point
from ..casting.objects import Objects


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.moved = 0
        self.score_val = 0

    def start_game(self, cast, objects, COLS, ROWS):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast, objects, COLS, ROWS)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.

        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast, objects, COLS, ROWS):
        """Updates the player's position and resolves any collisions with objects.

        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("score")
        player = cast.get_first_actor("player")
        stones = cast.get_actors("stones")
        gems = cast.get_actors("gems")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

        for stone in stones:
            stone.fall()
            p = stone.get_position()
            y = p.get_y()
            if y > 590:
                cast.remove_actor(stone)

            if player.get_position().equals(stone.get_position()):
                self.score_val - 100
                cast.remove_actor(stone)

        for gem in gems:
            gem.fall()
            p = gem.get_position()
            y = p.get_y()
            if y > 590:
                cast.remove_actor(gem)

            if player._position.equals(gem._position):
                self.score_val + 100
                cast.remove_actor(gem)

        # Create more
        if player._move_counter == 0:
            self.moved += 1

        if self.moved == 75:
            self.moved = 0
            objects.create_objects(cast, COLS, ROWS)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
