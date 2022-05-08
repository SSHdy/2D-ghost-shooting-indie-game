# 2D-ghost-shooting-indie-game
A 2D ghost shooting indie game for killing time during class break

for downloading the game, should modify the directory of the pictures in the code for the game to run successfully.

# Control
use W A S D on the keyboard to control the character and SPACE key to shoot the fireball for attack

# Key algorithm
The mobs in the game has an Artificial Intelligence Algorithm "State Machine" that make the mobs in the game have three States according to their distance to player
The first State is the randomly searching state. In a certain range when there is no player around them they will move randomly. The second state is hunting State. When they found out player is in their range they will move faster to search for the play. The third state is the attacking state. when the player is close enough, mobs will notice player and rush to the player.

# Tech Stack
This game is built with Python and Pygame.
