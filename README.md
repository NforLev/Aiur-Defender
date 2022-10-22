# Aiur-Defender
Python Starcraft themed space-shooter-game

Space shooter short 2d game using pygame

Shoot the enemys to get minerals (score), once you reach enough minerals new enemys will spawn
The game ends when any enemy reach the probe (player) line or hit the probe.

Each enemy has it's own class, with different X and Y speeds and the X movement is limited to the viewed screen,
when any enemy reach the screen limit it will change direction on the X axis and descend one move into Y axis,
this behavior is inhereted by all enemy classes from the main enemy class.
Each enemy gives different score based on how fast they are

Player movement is also limited to the X viewpoint and can shoot up to 4 projectiles

The projectiles the player shoot are created and appended into a list, you can shoot while list =< 4
when a projectile exit the screen, the projectile list pop one item, so you can shoot again

Each enemy class have a inhereted class method from the main enemy class to check if there's collision with any projectile 

There's a quick tutorial when you open the app with a pygame.wait of 4secs and then the game starts
When any enemy reach the probe line another pygame.wait starts to show a "thanks for playing" message and then game closes

Added some background sc1 music and game sound effects on shoot, enemy death and game start and sc font



png images from https://www.pngwing.com/
sound effects from http://nuclearlaunchdetected.com/
sc font from https://fontmeme.com/fonts/starcraft-font/
