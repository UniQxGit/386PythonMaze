#display array
def display_arr(arr = []):
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print (arr[i][j], end = " ")
		print ("")