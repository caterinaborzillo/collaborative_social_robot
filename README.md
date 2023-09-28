# RushHour: A Collaborative Social Robot 

Project for Reasoning Agents (Reasoning about Actions in Intelligent Autonomous Systems) and Human Robot Interaction courses at La Sapienza University of Rome (RA + HRI)

## Collaborators
Caterina Borzillo, Federica Cocci, Alessio Sfregola

## Project details
RushHour is a social and interactive robot for people’s entertainment. He plays with the human the
Rush Hour game in a collaborative way: human and robot work together to reach the goal making one move
alternately. The social interaction consists in an introductory presentation, in an initial and final surveys
and in different robot animations also during the game. The robot reasoning aspect is developed through
AIPlan4EU framework. The physical communication between the several components of the project has
been developed using a system of clients and servers.

- The reasoning aspect of our project has been implemented using a Python framework called AIPlan4EU. 

- Concerning human-robot interaction (HRI), we want to get the interaction between human and robot as natural as possible so our idea is to use our software on a physical robot called Pepper from the NAOqi robots family.

- However, we have tested our software only on a simulated Pepper and we use Choregraphe Suite as platform for the simulation (but sonars and verbal speaking tools from the physical NAOqi are not enabled in Choregraphe)

- Thanks to JavaScript (JS) and CSS and HTML, we created a web application to reproduce the Pepper tablet. This web application allows the user and the robot play together since the human can visualize the progress of the game and play the next move for solving the problem. Finally, in order to make all these components communicate with each other, we have exploited websockets and in order to implement them in Python we have used Tornado.