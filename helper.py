'''
    Created by:
    John Lee hyunmail94@csu.fullerton.edu
    Andre Victoria andrenaught@gmail.com
    Holly Ho hollyh@csu.fullerton.edu
    
    Description: helper with binary space partition algorithm to build maze
'''

import random

# Print out current maze
def display_arr(arr=[]):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print("")

# Creating class to hold the values of portal openings
class Coordinate:
    col = 0
    row = 0

    def __init__(self, col, row):
        self.row = row
        self.col = col

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col


# ************************************************
# Building maze using binary space partition
# @param arr - the socket from which to send
# @param portal_arr - array of all portals that have been opened
# @param cornerCellX - x coordinate corner cell of the existing array
# @param cornerCellY - y coordinate corner cell of existing array
# @param width
# @param height
# @return - new array with portal open
# *************************************************
def build_maze(arr=[], portal_arr=[], cornerCellX=0, cornerCellY=0, width=1, height=1):

    # Base of recursive call
    if (width == 1 and height == 1):
        return arr

    vertical = width > height
    splitLine = cornerCellX + random.randint(1, width - 1) * 2 if vertical else cornerCellY + random.randint(1,
                                                                                                             height - 1) * 2

    arr[cornerCellY][cornerCellX] = "o"

    portal = 0

    print("\nSplit Info: Vertical:", vertical, " splitLine:", splitLine)
    print("ORIGINAL:")
    print("Matrix Info:", "\n\tCorner Cell: (", cornerCellX, ",", cornerCellY, ")\n\tDimensions: ", width, "x", height);

    display_arr(arr);
    if (vertical):
        while portal == 0 or arr[portal][splitLine] == " ":
            portal = cornerCellY + (random.randint(1, height) * 2 - 1)
            print("PORTAL:", splitLine, ",", portal,)

        arr[portal][splitLine] = " "  # Replace with space

        widthOfFirstHalf = int((splitLine - cornerCellX) / 2)
        widthOfLastHalf = width - widthOfFirstHalf
        if (widthOfLastHalf < 1):
            widthOfLastHalf = 1
        heightOfFirstHalf = height
        heightOfLastHalf = height

        newCornerCellX = splitLine
        newCornerCellY = cornerCellY

        portal_arr.append(Coordinate(splitLine, portal))  # store these portal coordinates in array

    else:
        while portal == 0 or arr[splitLine][portal] == " ":
            portal = cornerCellX + random.randint(1, width) * 2 - 1
            print("PORTAL:", portal, ",", splitLine)
        arr[splitLine][portal] = " "  # Replace with space

        # Set new width/heights
        widthOfFirstHalf = width
        widthOfLastHalf = width
        heightOfFirstHalf = int((splitLine - cornerCellY) / 2)
        heightOfLastHalf = height - heightOfFirstHalf
        if (heightOfLastHalf < 1):
            heightOfLastHalf = 1

        newCornerCellX = cornerCellX
        newCornerCellY = splitLine

        portal_arr.append(Coordinate(portal, splitLine))  # store these portal coordinates in array

    print("NEW:")
    print("Matrix Info:", "\n\tFirst Half:\n\tDimensions:", widthOfFirstHalf, "x", heightOfFirstHalf)
    print("\tCornerCell (", cornerCellX, ",", cornerCellY, ")");

    print("\n\tLastHalf:\n\tDimensions", widthOfLastHalf, "x", heightOfLastHalf)
    print("\tCornerCell (", newCornerCellX, ",", newCornerCellY, ")");

    arr[newCornerCellY][newCornerCellX] = "o"
    display_arr(arr);

    arr = build_maze(arr, portal_arr, cornerCellX=cornerCellX, cornerCellY=cornerCellY, width=widthOfFirstHalf,
                     height=heightOfFirstHalf)  # first half
    arr = build_maze(arr, portal_arr, cornerCellX=newCornerCellX, cornerCellY=newCornerCellY, width=widthOfLastHalf,
                     height=heightOfLastHalf)  # last half

    return arr
