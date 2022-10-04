## This Readme file elaborate on how this script work as follow:
### main.py
1. First, the script will initalize main parameters and assign its value based on project requirement. For instance original score, win score, lost score and card value. See "def__init__(self)"

2. Second, the script will pass this value to function script that perform all the logic. See card(self) and receive return value from function script
to determine if score is 0 and then game is over. Additionally, it will prompt
the user, if they want to continue to play the game or not.

### function.py
1. The init function inherit all the objects from main.py script. Here, i assign it as "data".  See "def__init__(self,data)

2. display function will perform the logic which will prompt for user input,
read random value and do conditional check as in userInputCheck

3. userInputCheck, will read userinput and set the score value based on 
"h - High" and "l - Lower" parameters and then return the score to display

### To run this script 
python3 main.py

