FOOTBALL SEASON STATISTICS ANALYSIS SOFTWARE

INTRODUCTION

Welcome to Derin's football season statistics analysis software. The provided .csv file contains data for the 2021-2022 domestic season regarding the football teams in Europe's top 5 domestic leagues (England, Spain, Germany, Italy and France) and many values regarding their performance metrics. There are many performance metrics involved, football analysts use important metrics like xG and fan attendance numbers to draw conclusions regarding the teams and how many points they have gathered. This software can be used to draw significant conclusions about the teams and the leagues regarding these statistics.
Here are the performance metrics with their explanations:

LgRk - The team's rank in their domestic league based on points obtained in the season
MP - Amount of matches played in the season
W - Amount of wins in the season
D - Amount of draws in the season
L - Amount of loses in the season
GF - Goals scored
GA - Goals conceded
GD - Goal Difference (GF - GA)
Pts - Points obtained in the season
xG - Expected Goals - A metric that quantifies the quality of a scoring opportunity, indicating how likely it is for a particular shot to result in a goal based on various factors like shot angle, distance from the goal, type of assist, and more. It gives a number between 0 (no chance of scoring) and 1 (certain goal).
Attendance - Average fan attendance across the course of a season

Keep in mind that no output file is provided since when the program is ran it will by itself produce the output file with the name provided inside the same directory as where the python program is.

REQUIREMENTS

- Python 3.x
- math library
- pandas library

INSTALLATION

- If this is your first time using the pandas library, on your console please type pip install pandas.

RUNNING THE PROGRAM

Our program first asks the user for a file name that it will use to draw the data from, for this I have provided the required csv file that contains the statistics for the 2021 - 2022 domestic season. It is called 20212022Stats.csv.
Once this is entered the program will ask for a file name in the format of .....txt. It will use the provided filename to save the outputs later on. You can provide a simple input such as output.txt.
Then, a screen that explains each function and what they do and output gets displayed. Here, type a number between 1 and 8 and press enter. If you want to leave the program press 9. If you enter something other than these values the program will again as of you to provide an appropriate input.

Below, for each function case, I have provided inputs that you can type in order to test them:

1: 
1
Pts
All

2: 
2
Attendance
ENG

3: 
3
Pts
FRA

4: 
4
xG
ITA

5: 
5
Pts
ENG
51

6: 
6
Pts

7: 
7
Attendance
Wolves

8: 
8
xG
Pts

Finally, the displayed results are saved in the file that you have provided the name of.

TROUBLESHOOTING

- Ensure you have Python 3.x installed. You can check using python --version.

