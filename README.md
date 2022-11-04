## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                        (project root folder)
+-- greed                   (source code for game)
  +-- casting               (main object classes for game)
    +-- actor.py            (actor class and methods)
    +-- cast.py             (cast class and methods)
    +-- objects.py          (objects classes and methods also inherits actor class from actor.py)
  +-- directing             (main class to run game)
    +-- director.py         (director classs and methods)
  +-- services              (specific service classes)
    +-- keyboard_service.py (keyboard_service classes and methods)
    +-- video_service.py    (videoservice class and methods)
  +-- shared                (classes to help with visual effect and placement)
    +-- color.py            (color class and methods)
    +-- point.py            (point class and methods)
+-- __main__.py             (entry point for program)
+-- README.md               (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
 # McKay Thomas      (Built and adjusted the objects.py file and associated classes as well as the README)
 # Kylar Sorensen    (Built and adjusted the directer.py and associated classes. Outlayed the basic skeleton of the program with Brandon)
 # Zak Sattler       (Built and adjusted the main.py and video_service.py and the associated classes)
 # Brandon Smith     (Built and adjusted the cast.py and it's associated classes. Outlayed the basic skeleton of the program with Kylar)
 # Garret Cooper     (Built and adjusted the player.py and it's associated classes.)
