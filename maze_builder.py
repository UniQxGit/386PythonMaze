import helper

#test values
maze_width = 3
maze_height = 5

#array will include the walls and corners of the maze
array_width = (maze_width * 2) + 1
array_height = (maze_height * 2) + 1

#make empty array
maze = []
for i in range(array_height):
	maze.append([])
	for j in range(array_width):
		maze[i].append(0)

#putting walls and corners in maze
for row in range(len(maze)):		
	for col in range(len(maze[0])):
		if (row%2 == 0 and col%2 == 0):
			maze[row][col] = '+'
		elif (row%2 == 0 and col%2 == 1):
			maze[row][col] = '-'
		elif (row%2 == 1 and col%2 == 0):
			maze[row][col] = '|'
		elif (row%2 == 1 and col%2 == 1):
			maze[row][col] = ' '

maze = helper.build_maze(maze,cornerCellX=0,cornerCellY=0,width=maze_width,height=maze_height);

maze[1][1] = "S"
maze[array_height-2][array_width-2] = "X"

print ("\nFINAL:");
helper.display_arr(maze)

