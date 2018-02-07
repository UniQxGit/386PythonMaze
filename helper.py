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
	
	portal = random.randint(1,height)*2-1 if vertical else random.randint(1,width)*2-1;

	if(vertical):
		arr[portal][splitLine] = " " #Replace with space

		widthOfFirstHalf = splitLine/2
		widthOfLasthalf = width - widthOfFirstHalf
		heightOfFirstHalf = height
		heightOfLasthalf = height

		newCornerCellX = splitLine
		newCornerCellY = cornerCellY
	else:
		arr[splitLine][portal] = " " #Replace with space

		#Set new width/heights
		widthOfFirstHalf = width
		widthOfLasthalf = width
		heightOfFirstHalf = splitLine/2
		heightOfLasthalf = height - heightOfFirstHalf

		newCornerCellX = cornerCellX
		newCornerCellY = splitLine

	#arr = build_maze(arr,cornerCellX=cornerCellX,cornerCellY=cornerCellY,width=widthOfFirstHalf,height=heightOfFirstHalf) #first half
	#arr = build_maze(arr,cornerCellX=newCornerCellX,cornerCellY=newCornerCellY,width=widthOfLastHalf,height=heightOfLastHalf) #last half

	return arr

