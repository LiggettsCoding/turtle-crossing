Try and Cross the Road!
Infinite levels with scaling difficulty. This is a fairly basic Python code, but it was a great way to practice OOP and become comfortable in adding methods or attributes when needed, as well as learning how to have an intuitive thought process on solving the many problems I ran into.

screen.ontimer(register_key, 5000) on line 34 is not needed and can be taken out. This was an attempt to make the player wait for new cars to cover the road before moving on to a new level, but I decided to not use the clear_cars() method because it made the gameplay feel more fluid. Now, there is just a pause in the beginning so that the player can't race across the screen.

If you feel that there are too many cars on the screen, there is an easy fix for this. You will go to line 34 in main.py and change the randint range to a higher range. This will make it so that there is a lower chance of cars spawning.

If you feel that the cars are moving too fast and the speed curve is too high per level, then you can go to car_manager.py and lower the MOVE_INCREMENT. A MOVE_INCREMENT of 10 seemed to have a fun challenging experience, but I could definitely understand wanting to lower that.

If you want a bigger variety of colors for the cars, you could add colors from the turtle library to the COLORS list in car_manager.py.

That's all I've got for this one. I know it's simple, but it was a fun time to make. I hope you have fun!
