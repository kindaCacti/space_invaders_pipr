# SPACE INVADERS
This is a project for PIPR in Warsaw University of Technology:

AUTHOR: Mateusz Wawrzyniak

This project is a recreation of game called Space Invaders. In the game player tries to kill all the invaders before they get too close. To do that player controls a spaceship that can only go left or right and shoot. In this version I decided to make the game endless, and after shooting all enemies in single wave, another one spawns.

----------------------------------------

## Classes:
  - Entity
  - ShootingEntity
  - Bullet
  - Blocker
  - Enemy
  - Player
  - FileManager
  - Settings

## Class Entity:
  Describes every entity in the game using thier position, speed, size and image, which will be displayed on screen. Entities can move.

## Class ShootingEntity:
  Class that inherits from Entity, but also let's an entity shoot bullets and get hit by ones.

## Class Bullet:
  Class used to describe bullets. It inherits from Entity.

## Class Blocker:
  Inherits from ShootingEntity, because it can be shot. Blocker can be destroyed solely by the player. Blocker has 3 states of begin destroyed before it is broken.

## Class Enemy:
  Class describing every enemy in the game. They have a specific move pattern, so they can be offset and moved if specific criteria are met

## Class Player:
  Class used to represent Player. It inherits from ShootingEntity. This is the only entity that actual player can control during the game. It has shooting delay.

## Class FileManager:
  Class used to manage text files. It can read from them and write to them.

## Class Settings:
  Class containing main setting for the game

----------------------------------------

## HOW TO PLAY:
press A and D to move left and right. Press W to shoot. (holding W does not shoot multiple bullets)

----------------------------------------

### What I did do:
  - I implemented two different types of enemies.
  - I made sprites for every entity in the game
  - Implemented end screen and start screen
  - Made Blockers to be destroyed only by player

### What I didn't do:
  - I didn't write faster algorithm to detect bullet hits. It could've been O((n+m)log(n+m)) instead of O(n*m), where n is number of bullets and m is number of entities. I didn't implement this algorithm, because I don't think it is so useful in this project.

### What is different from first idea:
  - Different class distribution
  - Made images instead of circles and squares

----------------------------------------

## Thanks for checking out my project!