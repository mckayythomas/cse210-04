import os
import random
from tkinter.tix import ROW
from turtle import *


from greed.casting.actor import Actor
from greed.casting.objects import Objects
from greed.casting.cast import Cast

from greed.directing.director import Director

from greed.services.keyboard_service import KeyboardService
from greed.services.video_service import VideoService

from greed.shared.color import Color
from greed.shared.point import Point




FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = random.randint(9, 15)


def main():
    
    # create the cast
    cast = Cast()
    
    # create the score
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(5, 5)
    score = Actor()
    score.set_text("Player Score: ")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(position)
    cast.add_actor("score", score)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(450, 575)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
    


    # create the Gems
    x = int(MAX_X)
    y = int(MAX_Y)
    position = Point(random.randint(1,899), 0)
    gems = Actor()
    gems.set_font_size(FONT_SIZE)
    gems.set_position(position)
    cast.add_actor("gems", gems)


    # # create the Rocks
    x = int(MAX_X)
    y = int(MAX_Y)
    position = Point(random.randint(1,899), 0)
    rocks = Actor()
    rocks.set_font_size(FONT_SIZE)
    cast.add_actor("rocks", rocks)

    

    for n in range(DEFAULT_ARTIFACTS):
        
        picker = random.randint(1,2)
        if picker == 1:
            text = ('*')
        elif picker == 2:
            text = ('o')
        

        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        object = Objects()
        object.set_text(text)
        object.set_font_size(FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        cast.add_actor("objects", object)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()