# Super Awesome Battleship - THE GAME

## Description  

 A retro looking, simple battleship game.
The rules:

- O repsents the ocean on the board
- X means that the player has missed
- The player can only have 10 turns. If the player has run out of turns the a message will show saying "Game Over"
- If the player has guessed the same row and column, a message will appear "You guessed that one already" and they will lose a turn
- The player can only user numbers from 0 - 8 to guess rows and columns

<hr>

### Features

![](assets/imgs/Screenshot%20(114).png)
- The grid
  - It is 8*8
  - The Os represent the rows and column or the ocean

<hr>

### How to play
- The player starts the game with 10 turns or guess
- The game will first ask the player to guess the row, it only accepts inputs of 0-8, then it will ask the player to guess the column
- 
<hr>

### Bugs & Fixes

- Guess_row infinity loop
  - Even if the player inputs numbers, it will keep asking for an input. The player will have to press "enter" twice in order for the loop to stop and continue.
    - I have not been able to find a fix for this bug
![](assets/imgs/pp3_bug_gif.gif)

### Planning & Design

For the game I wanted to go full on old school. Just a simple grid with Xs and Os.
![luccidchart](assets/imgs/PP3%20Python.jpeg)

<hr>

## Credit

### Programs used

#### Notetaking & Planning

- Obsidian
  - It is an interesting productivity application. It is a Markdown-based system that incorporates tags, plugins and back-links to create a compelling to use system. Great tool for note-taking and planning out projects. Later you can export your notes as PDFs.

#### Langueges used

- Python
  - The Battleship was created using Python.  

#### Code 

- Code was inspired by this tutorial <https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=732s> by Knowledge Mavens

#### Gif
- clideo.com was used in order to crop and convert my video