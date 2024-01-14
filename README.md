# [TEXTBASED QUARTERBACK GAME](https://textbased-quarterback-game-fcaaa3679ab0.herokuapp.com)

Textbased Quarterback Game is an engaging and strategic text-based simulation game that puts you in the shoes of a quarterback. As the quarterback, you make critical decisions on the field, leading your team to victory. The game focuses on the strategic aspects of football, allowing you to choose plays, make split-second decisions, and experience the thrill of the game.

![screenshot](documentation/mockup.png)


## UX
Welcome to the immersive world of QB1, where you become the quarterback for the New York Giants in the Super Bowl showdown against the Kansas City Chiefs. To ensure an enjoyable user experience, I've incorporated deliberate time delays using `time.sleep(2)` to prevent information overload and keep you engaged at every step.

Throughout the game, you'll find yourself in the midst of intense moments, with a scoreboard providing real-time updates on the score and possession counters keeping you informed about the game's progress. Decision-making is key, and your choices, such as selecting plays and calling coin tosses, will shape the destiny of your team.

Strategic elements like the last possession and overtime scenarios add an extra layer of excitement. Witness the final scores, complete with congratulatory messages for victories or encouraging words in case of a setback. When the game concludes, easily navigate back to the main menu for a swift replay.

QB1 is not just a game; it's an experience crafted with your enjoyment in mind. Your feedback is invaluable, so let's dive into the world of QB1 and create memorable adventures on the virtual gridiron!


## User Stories

### New Site Users

- As a new site user, I want to easily understand how to play the game so that I can start enjoying it quickly.
- As a new site user, I want clear instructions on how to make decisions in the game so that I can play effectively.
- As a new site user, I want an engaging and immersive experience while playing the game.
- As a new site user, I want feedback on my decisions so that I can learn and improve my gameplay.
- As a new site user, I want the game to be challenging and dynamic, providing a sense of accomplishment when I succeed.

### Returning Site Users
- As a returning site user, I want to play the game again, with different outcomes
- As a returning site user, I want to explain the game to my friends (rules provided)


## Features

### Existing Features

| Feature | About | Image |
| --- | --- | --- |
| **Quarterback Decision Making:** | From the coin toss to the last decisive pass. There are no limits to the thrill of countless 50/50 decisions in this game. Simple user inputs (predefined numbers) are used to play different scenarios that result from the user's decisions. | ![screenshot](documentation/feature01.png) |
| **Scoreboard:** | The scoreboard is updated after each possession and displayed to the user before each new team possession, so the user knows the current score at all times. | ![screenshot](documentation/feature02.png) |
| **User Possession Counter:** | With the user possession counter, the user always knows how many attempts he has left until the game is over. This is because the game is exactly 7 possessions long, which the user can also check in the rules. | ![screenshot](documentation/feature03.png) |
| **The Rulebook:** | The rulebook provides a brief but easy-to-follow overview of what the game is about, how long the game lasts and how it works. | ![screenshot](documentation/feature04.png) |
| **Easy User Navigation:** | As already mentioned, the user can navigate through the entire game using simple user inputs. Each input is preceded by a detailed explanation of the consequences of entering a particular number. | ![screenshot](documentation/feature05.png) |

### Future Features

- Implement game history and statistics to track progress for returning site users.
- A chance to select between several teams to play with.


## Tools & Technologies Used

- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.


## Data Model

### Flowchart

![screenshot](documentation/flowchart.png)

### Classes & Functions

The primary functions used on this application are:

| Function | What it does |
| --- | --- |
| `welcome()` | Function to display the menu of the game and welcome the sites user. |
| `user_choice_welcome()` | Function to let user decide between starting the game or reading the rules. |
| `game_rules()` | Function to display rules and let user decide if he wants do get back to menu or start game directly (navigation function). |
| `game_rules_navigation()` | Function to let user navigate back to the main menu or start the game while in the rules. |
| `start_game()` | Function to start the game. The game starts with the first decission: the cointoss! |
| `cointoss_start_game()` | Function to start the game with the first decission: the cointoss! |
| `chiefs_posession()` | Function when chiefs are in posession. USER HAS NO CONTROL! |
| `giants_possession()` | Function when the Giants (The User) is in possession of the ball with random starting position and yard line. |
| `giants_posession_choose_play()` | Function for user to decide what play to be played. |
| `end_game()` | Function for the end of the game. |
| `start_overtime()` | Function for overtime to start, when game ended in a draw. |
| `chiefs_posession_overtime()` | Function for chiefs possession in overtime. |
| `giants_possession_overtime()` | Function for the user possession to start. |
| `giants_posession_choose_play_overtime()` | Function for the user Quarterback choices in overtime. |
| `coin_toss_overtime()` | Function for the cointoss in overtime. |
| `end_game_after_overtime()` | Function to end the game after overtime. |
| `end_game_navigation ()` | Function to let user navigate back to the main menu. |

### Imports

I've used the following Python packages and/or external imported packages.

- `time`: used for delayed responses for better user overview
- `random`: used for random scenario outcomes in the game


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.


## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://textbased-quarterback-game-fcaaa3679ab0.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/firstnamejonas/textbased-quarterback-game) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/firstnamejonas/textbased-quarterback-game.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/firstnamejonas/textbased-quarterback-game)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/firstnamejonas/textbased-quarterback-game)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

The local version may have additional debug features enabled for testing purposes. It's recommended to use the deployed version for the best user experience.


## Credits

### Content

| Source | Usage |
| --- | --- |
| [W3Schools](https://www.w3schools.com) | for various tutorials on Python |
| [YouTube](https://www.youtube.com) | for tutorials on game development concepts. |
| [WikiHow](https://www.wikihow.com/Write-a-Coin-Flipping-Program-on-Python) | for tutorial on how to implement the cointoss into the game |
| [DigitalOcean](https://www.digitalocean.com/community/tutorials/python-time-sleep) | for time.sleep() function to hold back responses for a better user overview |
| [StackOverflow](https://stackoverflow.com/questions/46820182/randomly-generate-1-or-1-positive-or-negative-integer) | for implementation of randomly generated scenario outcome |

### Acknowledgements

- I would like to thank my family & my partner Caro, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project, giving me confidence and valuable advice!
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going.
