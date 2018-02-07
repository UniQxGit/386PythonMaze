import random

#display array
def display_arr(arr = []):
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print (arr[i][j], end = " ")
		print ("")

#I'm not entirely sure how to define paramaters yet, but this seems to work.
def build_maze(arr = [], cornerCellX = 0, cornerCellY = 0, width = 1, height = 1):
	if(width == 1 and height == 1):
		return arr
	vertical = width > height
	splitLine = cornerCellX+random.randint(1,width-1)*2 if vertical else cornerCellY+random.randint(1,height-1)*2
	arr[splitLine][cornerCellY] = "o"
	print ("From builder:\n","Vertical:",vertical," splitLine:",splitLine)
	return arr

