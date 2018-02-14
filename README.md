# Project # 1 - Python Maze #
## Team info ##
Class Number: CPSC 386-01 13263

Team Name: LHV

Team:

	John Lee
  
	Holly Ho
  
	Andre Victoria

Intro:

For our python maze, we used the binary space partition algorithm.

The algorithm consists of the following steps:

1. Pick split orientation, either horizontal or vertical
2. Pick the row to split on
3. Use that row to split the maze into two regions
4. Pick a portal to take away from the row that you split on. Add that portal to a list to keep track of the portals we created.
5. Recursively call the function on the two new regions of the maze that is formed from the split line
6. The base case of the recursion: return when the width and height of the new regions are 1

## Getting Started ##

Contents:

1. helper.py
2. maze_builder.py
3. README.txt

External Requirements: Python3

Setup and Installation:
No installation required.

1. Open Command Line/Terminal and change directory into the project folder.
2. type "python3 maze_builder.py" and press enter.

## Sample Invocation and results to see##

python3 maze_builder.py
Input maze width: 3
Input maze height: 3

Split Info: Vertical: False  splitLine: 2
ORIGINAL:
Matrix Info:
Corner Cell: ( 0 , 0 )
Dimensions:  3 x 3
o - + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
PORTAL: 1 , 2
NEW:
Matrix Info:
First Half:
Dimensions: 3 x 1
CornerCell ( 0 , 0 )

LastHalf:
Dimensions 3 x 2
CornerCell ( 0 , 2 )
o - + - + - +
|   |   |   |
o   + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +

Split Info: Vertical: True  splitLine: 2
ORIGINAL:
Matrix Info:
Corner Cell: ( 0 , 0 )
Dimensions:  3 x 1
o - + - + - +
|   |   |   |
o   + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
PORTAL: 2 , 1
NEW:
Matrix Info:
First Half:
Dimensions: 1 x 1
CornerCell ( 0 , 0 )

LastHalf:
Dimensions 2 x 1
CornerCell ( 2 , 0 )
o - o - + - +
|       |   |
o   + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +

Split Info: Vertical: True  splitLine: 4
ORIGINAL:
Matrix Info:
Corner Cell: ( 2 , 0 )
Dimensions:  2 x 1
o - o - + - +
|       |   |
o   + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
PORTAL: 4 , 1
NEW:
Matrix Info:
First Half:
Dimensions: 1 x 1
CornerCell ( 2 , 0 )

LastHalf:
Dimensions 1 x 1
CornerCell ( 4 , 0 )
o - o - o - +
|           |
o   + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +

Split Info: Vertical: True  splitLine: 2
ORIGINAL:
Matrix Info:
Corner Cell: ( 0 , 2 )
Dimensions:  3 x 2
o - o - o - +
|           |
o   + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
PORTAL: 2 , 3
NEW:
Matrix Info:
First Half:
Dimensions: 1 x 2
CornerCell ( 0 , 2 )

LastHalf:
Dimensions 2 x 2
CornerCell ( 2 , 2 )
o - o - o - +
|           |
o   o - + - +
|       |   |
+ - + - + - +
|   |   |   |
+ - + - + - +

Split Info: Vertical: False  splitLine: 4
ORIGINAL:
Matrix Info:
Corner Cell: ( 0 , 2 )
Dimensions:  1 x 2
o - o - o - +
|           |
o   o - + - +
|       |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
PORTAL: 1 , 4
NEW:
Matrix Info:
First Half:
Dimensions: 1 x 1
CornerCell ( 0 , 2 )

LastHalf:
Dimensions 1 x 1
CornerCell ( 0 , 4 )
o - o - o - +
|           |
o   o - + - +
|       |   |
o   + - + - +
|   |   |   |
+ - + - + - +

Split Info: Vertical: False  splitLine: 4
ORIGINAL:
Matrix Info:
Corner Cell: ( 2 , 2 )
Dimensions:  2 x 2
o - o - o - +
|           |
o   o - + - +
|       |   |
o   + - + - +
|   |   |   |
+ - + - + - +
PORTAL: 5 , 4
NEW:
Matrix Info:
First Half:
Dimensions: 2 x 1
CornerCell ( 2 , 2 )

LastHalf:
Dimensions 2 x 1
CornerCell ( 2 , 4 )
o - o - o - +
|           |
o   o - + - +
|       |   |
o   o - +   +
|   |   |   |
+ - + - + - +

Split Info: Vertical: True  splitLine: 4
ORIGINAL:
Matrix Info:
Corner Cell: ( 2 , 2 )
Dimensions:  2 x 1
o - o - o - +
|           |
o   o - + - +
|       |   |
o   o - +   +
|   |   |   |
+ - + - + - +
PORTAL: 4 , 3
NEW:
Matrix Info:
First Half:
Dimensions: 1 x 1
CornerCell ( 2 , 2 )

LastHalf:
Dimensions 1 x 1
CornerCell ( 4 , 2 )
o - o - o - +
|           |
o   o - o - +
|           |
o   o - +   +
|   |   |   |
+ - + - + - +

Split Info: Vertical: True  splitLine: 4
ORIGINAL:
Matrix Info:
Corner Cell: ( 2 , 4 )
Dimensions:  2 x 1
o - o - o - +
|           |
o   o - o - +
|           |
o   o - +   +
|   |   |   |
+ - + - + - +
PORTAL: 4 , 5
NEW:
Matrix Info:
First Half:
Dimensions: 1 x 1
CornerCell ( 2 , 4 )

LastHalf:
Dimensions 1 x 1
CornerCell ( 4 , 4 )
o - o - o - +
|           |
o   o - o - +
|           |
o   o - o   +
|   |       |
+ - + - + - +

FINAL:
o - o - o - +
| S         |
o   o - o - +
|           |
o   o - o   +
|   |     X |
+ - + - + - +

Portals opened (in sequence):
[ row:  2 | col:  1 ]
[ row:  1 | col:  2 ]
[ row:  1 | col:  4 ]
[ row:  3 | col:  2 ]
[ row:  4 | col:  1 ]
[ row:  4 | col:  5 ]
[ row:  3 | col:  4 ]
[ row:  5 | col:  4 ]


## Features ##
 * No extra features, simply outputs on screen a randomized maze.

Bugs: None found.
