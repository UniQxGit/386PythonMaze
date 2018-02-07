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
	#vertical = 
	splitLine = cornerCellX+random.randint(1,width-1)*2 if vertical else cornerCellY+random.randint(1,height-1)*2
	
	
	arr[cornerCellY][cornerCellX] = "o"
	
	#TODO: make sure that the portal isn't already open
	portal = 0;#random.randint(1,height)*2-1 if vertical else random.randint(1,width)*2-1;
	
	print ("\nSplit Info: Vertical:",vertical," splitLine:",splitLine)
	print ("ORIGINAL:")
	print ("Matrix Info:","\n\tCorner Cell: (", cornerCellX, ",",cornerCellY,")\n\tDimensions: ",width,"x", height);
	
	display_arr(arr);
	if(vertical):
		while portal == 0 or arr[portal][splitLine] == " ":
			portal = cornerCellY + (random.randint(1,height)*2-1)
			print("PORTAL:",portal);
			#portal %= 

		arr[portal][splitLine] = " " #Replace with space

		widthOfFirstHalf = int((splitLine-cornerCellX)/2)
		widthOfLastHalf = width - widthOfFirstHalf
		if(widthOfLastHalf < 1):
			widthOfLastHalf = 1
		heightOfFirstHalf = height
		heightOfLastHalf = height

		newCornerCellX = splitLine
		newCornerCellY = cornerCellY

	else:
		while portal == 0 or arr[splitLine][portal] == " ":
			portal = cornerCellX + random.randint(1,width)*2-1
			print("PORTAL:",portal);
		arr[splitLine][portal] = " " #Replace with space

		#Set new width/heights
		widthOfFirstHalf = width
		widthOfLastHalf = width
		heightOfFirstHalf = int((splitLine-cornerCellY)/2)
		heightOfLastHalf = height - heightOfFirstHalf
		if(heightOfLastHalf < 1):
			heightOfLastHalf = 1

		newCornerCellX = cornerCellX
		newCornerCellY = splitLine

		


	print ("NEW:")
	print ("Matrix Info:" ,"\n\tFirst Half:\n\tDimensions:",widthOfFirstHalf, "x",heightOfFirstHalf)
	print ("\tCornerCell (", cornerCellX,",", cornerCellY,")");

	print ("\n\tLastHalf:\n\tDimensions",widthOfLastHalf, "x",heightOfLastHalf)
	print ("\tCornerCell (", newCornerCellX,",", newCornerCellY,")");
	
	arr[newCornerCellY][newCornerCellX] = "o"
	display_arr(arr);
	
	arr = build_maze(arr,cornerCellX=cornerCellX,cornerCellY=cornerCellY,width=widthOfFirstHalf,height=heightOfFirstHalf) #first half
	arr = build_maze(arr,cornerCellX=newCornerCellX,cornerCellY=newCornerCellY,width=widthOfLastHalf,height=heightOfLastHalf) #last half

	return arr

