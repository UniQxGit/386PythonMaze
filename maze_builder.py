'''
    Created by:
    John Lee hyunmail94@csu.fullerton.edu
    Andre Victoria andrenaught@gmail.com
    Holly Ho hollyh@csu.fullerton.edu
    
    Description:
    Creating a maze based on the height and width the user picks
'''

import helper

# take in user input
maze_width = int(input("Input maze width: "))
maze_height = int(input("Input maze height: "))

# test values
# maze_width = 3
# maze_height = 5

# Array will include the walls and corners of the maze
array_width = (maze_width * 2) + 1
array_height = (maze_height * 2) + 1

# Creating array to hold maze
maze = []
for i in range(array_height):
    maze.append([])
    for j in range(array_width):
        maze[i].append(0)

# Creating the base of the maze
# Building the walls and corners
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if (row % 2 == 0 and col % 2 == 0):
            maze[row][col] = '+'
        elif (row % 2 == 0 and col % 2 == 1):
            maze[row][col] = '-'
        elif (row % 2 == 1 and col % 2 == 0):
            maze[row][col] = '|'
        elif (row % 2 == 1 and col % 2 == 1):
            maze[row][col] = ' '

# Array to hold the portal openings of maze
portal_arr = []

# Calling build_maze function to create maze with portals
maze = helper.build_maze(maze, portal_arr, cornerCellX=0, cornerCellY=0, width=maze_width, height=maze_height);

# Labeling start and finish of maze
maze[1][1] = "S"
maze[array_height - 2][array_width - 2] = "X"

print("\nFINAL:");
helper.display_arr(maze)

# Displaying portals created
print("\nPortals opened (in sequence):")
for i in range(len(portal_arr)):
    print("[ row: ", portal_arr[i].get_row(), "| col: ", portal_arr[i].get_col(), "]")

print("\n")
