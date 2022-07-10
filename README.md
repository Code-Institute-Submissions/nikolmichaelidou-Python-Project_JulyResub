# Super Awesome Battleship - THE GAME

## Description  

 A retro-looking, simple battleship game.
It is a Python terminal game. Made to look and feel like one those first games.
The goal is to guess the location the battleship. The player has only 10 turns to do so.
It is aimed at any specific audience. Any one can enjoy!

<hr>

### Features

- 10x10 grid 
- 8 ships of variable length randomly placed about
- Player has 50 bullets to take down the ships that are placed down
  - Player can choose a row and column such as A3 to indicate where to shoot
    - For every shot that hits or misses it will show up in the grid

Below are symbols used to represent obstacles or components in the game:
- "." = water or empty space
- "O" = part of ship
- "X" = part of ship that was hit with a bullet
- "#" = water that was shot with a bullet, a miss because it hit no ship

<hr>

### How to play
The game is very easy to play. Requires very minimal controls. The player simply types numbers.
- The player only has 50 bullets
- There are two ships on the grid
  - The player must sink them before they run out of bullets
- The player can guess the placement of this ships using letters and numbers, for example such us A5  

<hr>

### Bugs & Fixes
I have manually tested the game and these are the following bugs I've encountered: 
- Guess_row infinity loop
  - Even if the player inputs numbers, it will keep asking for input. The player will have to press "enter" twice for the loop to stop and continue.
    - I have not been able to find a fix for this bug
![](assets/imgs/pp3_bug_gif.gif)

- 'yes' or 'no' bug
  - In order for the function it the player will either have to type 'yes' or 'no' without space. Which looks weird.
  - The bug was fixed by simply fixing a small typo in the code
![](assets/imgs/Screenshot%20(119).png)

- The bugs have been fixed:
  - Rewrote the entire code, the main changes are
    - From a 8x8 grid I made it to a 10x10 grid
    - The player can see a part of the ships now

### Planning & Design
Rough outline of the game:
![](assets/imgs/PP3-rough-outline.jpg)
For the game, I wanted to go full-on old school. Just a simple grid with Xs and Os.
- The logic of the game was dumb down, make as simple as possible so it will be easier to build into as the project progessed. As shown in the flowchart:
![luccidchart](assets/imgs/PP3%20Python.jpeg)

<hr>

## Validator testing
- PEP8 was used to validate the code
  - In order to make sure there were no issues with the code:
    - I've tested every section of the code before committing
      - The only error that was returned was that the comments were too long
 ![](/assets/imgs/Screenshot%20(136).png)

<hr>

## Deployment
The below steps were followed to deploy this project to Heroku:

- Go to Heroku and click "New" to create a new app.
- After choosing the app name and setting the region, press "Create app".
- Go to "Settings" and navigate to Config Vars. Add a Config Var with a key word of called PORT and a value of 8000.
- Still in the "Settings", navigate to Buildpacks and add buildpacks for Python and NodeJS. They have to be in order, Python first, then NodeJS.
- Go to "Deploy". Scroll down and set Deployment Method to GitHub. Once GitHub is chosen, find your repository and connect it to Heroku.
- Scroll down to Manual Deploy, make sure the "main" branch is selected and click "Deploy Branch".
- The deployed app can be found here <https://battleshipci.herokuapp.com/>

## Credit

### Programs used
 - Xbox Games Bar was used to record the screen and then used clideo.com was used to crop and convert my video
 - LucidChart was used to create the flow chart

#### Notetaking & Planning

- Obsidian
  - It is an interesting productivity application. It is a Markdown-based system that incorporates tags, plugins, and back-links to create a compelling to use the system. Great tool for note-taking and planning out projects. Later you can export your notes as PDFs.

#### Langueges used

- Python was used to create the game. 

#### Code 

- Code was inspired by these tutorials by Knowledge Mavens. 
  -  <https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=732s>
  -  <https://www.youtube.com/watch?v=alJH_c9t4zw> 

