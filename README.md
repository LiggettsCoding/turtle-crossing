# turtle-crossing
try and cross the road! Infinite levels with scaling difficulty. 
this is some fairly basic python code, but it was a great way to practice OOP 
to be able to become comfortable in adding methods or atributes when needed
and learning how to have a intuitive thought process on solving the many problems i ran into.
screen.ontimer(register_key, 5000) on line 34 is not needed and can be taken out. This was an
attempt to make the player wait for new cars to cover the road before moving on a new level,
but i decided to not use the clear_cars() method because it made the gameplay feel more fluid
so now there is just a pause in the beggining so that the player cant race across the screen
if you feel that there are to many cars on the screen there is an easy fix for this
you will go to line 34 in main.py and change the randint range to a higher range
this will make it were there is a lower chance of cars spawning.
if you feel that the cars are moving to fast and the speed curve is to high per level
then you can go to car_manager.py and lower the MOVE_INCREMENT.
a MOVE_INCREMENT of 10 seemed to have a fun challenging experience, but i could def understand
wanting to lower that
if youd want a bigger variety of colors for the cars you could add colors from the turtle library
to the COLORS list in car_manager.py
thts all i got for this one. I know its simple but it was a fun time to make. 
I hope you have fun!
