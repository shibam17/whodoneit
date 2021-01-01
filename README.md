# whodoneit
#### Available live at:[crimescene.study](https://crimescene.study/)
### Inspiration
We'll are great fans of Sherlock Holmes and Robert Langdon for their big brain solving the hardest of the hardest mysteries.So our team decided to give you a similar experience at home to play around with your friends.

### What it does
Sherlock HOME is a game of solving clues and finding the ultimate lost mystery.So we have both hardware versions and software versions of the game.The game is to played between a group of people.The host has to hide the clue code. Upon finding the clue code the player has to input the code in the website/hardware and he'll get the next clue
In the software part we have a website where the clues are given.The host has to hide the clue codes in different parts of the house.Upon finding a clue code he/she has to enter the code on our website and he'll get the next clue if he is correct or has to retry again
For the hardware part.We have made a device using a Raspberry Pi to handle the game.The clues will be send to the players via SMS using the twilio API.When the player finds a clue code he has to enter the code in the raspbery pi using a Keypad to and the information is shown in a 16*2 LCD screen.Additionally we have made a device for making the game more interesting,since the house is particularly a large area and has dozen of places to hide clue codes.We created a clue finder using Arduino,IR transmitter and receiver. So that players can use it to know whether he/she is near a clue code and this adds more fun to the game

### How we built it
#### Software
For the website we made the front end to show the clues and to enter the Clue codes using HTML,CSS & Js.The clues are fetched from a custom API made in Flask.So we compare the users inputted clue code with the actual clue codes and fetch clues accordingly
#### Hardware
We've used a Raspberry Pi,16*2 LCD module (we required a 4*4 matrix keypad module but due to unavailability we went with the normal keyboard for inputting) to show the information.When the game starts the clue is sent via SMS using Twilio API to the players phone and when the players gives the correct clue code he receives the next clue. For the clue code detector we've used an Arduino along with an IR transmitter receiver pair and piezo buzzer to make a standalone device.So the host has to place IR transmitters near the places he has hidden the clue codes so that when the player comes anywhere in the range of the IR transmitter he gets a beep in the device and he can know whether he is close.So in our hack we have used a normal IR remote as the transmitter.
### Challenges we ran into
It was our first time interfacing a 16*4 LCD module with a raspberry Pi.
Make a different questions according to the common things found at home
Using the IRremote.h and tone() library at the same time gave timer error which took a long time to debug
Using IR receiver
### Accomplishments that we're proud of
We are super excited that we could implement the hack as planned
Met new people and could collaborate on a project this weekend
We did actually try a demo game and it worked out very well with the hardware.
### What we learned
How to interface a 16*2 LCD with a Raspberry PI
Different modes for an LCD module
Interfacing an IR receiver with an Arduino
### What's next for Sherlock HOME
Use IR transmitting LEDs
UI improvements with the website.

#### Hackathon  13 Dec 2020
