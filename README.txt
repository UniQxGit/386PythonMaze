Project # 1 - Python Maze
Class Number: CPSC 386-01 13263

Team Name: LHV

Team members:

	John Lee
	Holly Ho
	Andre Victoria

Intro:

For our python maze, we used the binary space partition algorithm.

The algorithm consists of the following steps:

	1. Pick split orientation, either horizontal or vertical
	2. Pick the row to split on
	3. Use that row to split the maze into two regions
	4. Pick a portal to take away from the row that you split on. Add that portal to a 	list to keep track of the portals we created.
	5. Recursively call the function on the two new regions of the maze that is formed 	from the split line
	6. The base case of the recursion: return when the width and height of the new 		regions are 1


Contents:
	1. helper.py
	2. maze_builder.py
	3. README.txt

External Requirement
	Python3

Setup and Installation
	No installation required.

To run program:
1. Open Command Line/Terminal and change directory into the project folder.
2. type "python3 maze_builder.py" and press enter.

Sample Invocation and results to see

	Refer to sampleOutput.txt to see sample invocation

Features
	No extra features, simply outputs on screen a randomized maze.

Bugs
	None found.
