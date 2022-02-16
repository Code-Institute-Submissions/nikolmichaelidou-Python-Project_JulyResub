# Super Awesome Battleship - THE GAME

## Description  

 A retro-looking, simple battleship game.
The rules:

- O represents the ocean on the board
- X means that the player has missed
- The player can only have 10 turns. If the player has run out of turns a message will show saying "Game Over"
- If the player has guessed the same row and column, a message will appear "You guessed that one already" and they will lose a turn
- The player can only use numbers from 0 - 8 to guess rows and columns

<hr>

### Features

- The grid
  - It is 8*8
  - The Os represent the rows and columns or the ocean
![](assets/imgs/Screenshot%20(114).png)

- Welcome message
  - A brief welcome message will appear welcoming the player
  - And also a brief message mentioning how many turns the player has 
![](assets/imgs/Screenshot%20(116).png)

- Error messages
 - 

<hr>

### How to play
- The player starts the game with 10 turns or guess
- The game will first ask the player to guess the row, it only accepts inputs of 0-8, then it will ask the player to guess the column
- If the player guesses the same combination a message will pop saying "You guessed that one already."
<hr>

### Bugs & Fixes
I have manually tested the game and these are the following bugs I've encountered: 
- Guess_row infinity loop
  - Even if the player inputs numbers, it will keep asking for input. The player will have to press "enter" twice for the loop to stop and continue.
    - I have not been able to find a fix for this bug
![](assets/imgs/pp3_bug_gif.gif)

### Planning & Design

For the game, I wanted to go full-on old school. Just a simple grid with Xs and Os.
- Firstly, was dumb down the logic of the game, make as simple as possible so it will be easier to build into as the project progessed.
- Secondly
![luccidchart](assets/imgs/PP3%20Python.jpeg)

<hr>

## Deployment
The below steps were followed to deploy this project to Heroku:

- Go to Heroku and click "New" to create a new app.
- After choosing the app name and setting the region, press "Create app".
- Go to "Settings" and navigate to Config Vars. Add a Config Var with a key word of called PORT and a value of 8000.
- Still in the "Settings", navigate to Buildpacks and add buildpacks for Python and NodeJS. They have to be in order, Python first, then NodeJS.
- Go to "Deploy". Scroll down and set Deployment Method to GitHub. Once GitHub is chosen, find your repository and connect it to Heroku.
- Scroll down to Manual Deploy, make sure the "main" branch is selected and click "Deploy Branch".
- The deployed app can be found here.

## Credit

### Programs used
 - Heroku was used to deploy the game to the web.
 - Xbox Games Bar was used to record the screen and then used clideo.com was used to crop and convert my video
 - LucidChart was used to create the flow chart

#### Notetaking & Planning

- Obsidian
  - It is an interesting productivity application. It is a Markdown-based system that incorporates tags, plugins, and back-links to create a compelling to use the system. Great tool for note-taking and planning out projects. Later you can export your notes as PDFs.

#### Langueges used

- Python was used to create the game. 

#### Code 

- Code was inspired by this tutorial <https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=732s> by Knowledge Mavens.
