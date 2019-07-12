# Overwatch-PUG-BOT
Overwatch PUG BOT for 6v6s and 2v2s.

## No License 
No license was included in this project for a reason. Do not download and run this code - although you may view it through github. 

## About
This project is very old and was one of the first Python *applications* I properly wrote. Of course there are many code inaccuracies as I was (relatively) new to Python and this happened to be one of the most "unexpectedly" bloated projects I've ever completed. Overwatch PUG BOT was made in two weeks and aimed to add some sort of "server-like" framework to Overwatch, a game known to be devoid of proper private servers. The bot works entirely off of screen reading and analysis as well as keyboard/ mouse hooks. To achieve desired results, Google's Tesseract OCR neural network was used. 

## What does the bot running look like?
In some ways, it is quite similar to something like ESEA in terms of what players experience. The bot will start and is set to begin at the Overwatch main menu screen. It navigates over to the custom games section and creates a game with a specific PUG-warmup preset. It then invites the players who will play into the game. 

Warmup is a simple FFA where players have a change to, well, warmup before the main game. Once a player is ready, they type `%ready` into the chat and the bot will read this and record the player as being ready. Once all 12 (or 4) players are ready, the match is set to start; the bot sends everyone back to the main lobby, changes the preset, sorts the teams out (as well as team names!) and the game is officially started. 

Once in the game, players can call for a `%pause%` and `%unpause%` which does what is expected. They play until someone wins, where again the screen is read and parsed so the winning data is reflected by the bot. The game returns to the lobby and the bot leaves the game, returning to the main menu.

#### Special thanks
As you might imagine, a project like this requires lots, and lots, and lots of testing. What's even worse is that the environment in which this project took place (Overwatch) is so inflexible that at some stage I simply could not continue work unless there really were real players in the lobby. So, I would like to thank my friends and beta-testers who helped out immensely with the testing process: Hazz, Matt, Mattie, Michael, Jacky, and Robby.
