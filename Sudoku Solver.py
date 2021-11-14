# Author: Nik Delgado
# Date: 11/14/21
# Program: Sudoku Solver
# Description: This program solves a sudoku puzzle using the backtracking algorithm

board = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# This function prints out the board array to console
def print_board(bo):
	for i in range(len(bo)):
		
		if i % 3 == 0 and i != 0:
			print("-----------------------")
			
		for j in range(len(bo[i])):
			if j % 3 == 0 and j != 0:
				print (" | ", end="")
				
			print(bo[i][j], end=" ")
		
		print("")
		
# This function returns the position of an empty slot on the board
def get_empty_slot(bo):
	for row in range(len(bo)):
		for col in range(len(bo[row])):
			if (bo[row][col] == 0):
				return row, col
			
	row = None
	col = None
	return row, col
	
# This function takes in a number and checks if the number is valid to place in the given position on the sudoku board
def check_valid(bo, row, col, num):
	
	# Check Row
	for i in range(len(bo[row])):
		if (bo[row][i] == num):
			return False

	# Check Column
	for i in range(len(bo[col])):
		if (bo[i][col] == num):
			return False

	# Check Quadrant
	quadrant_row = row // 3
	quadrant_col = col // 3

	for i in range(quadrant_row * 3, quadrant_row * 3 + 3):
		for j in range(quadrant_col * 3, quadrant_col * 3 + 3):
			if (bo[i][j] == num):
				return False
		
	
	return True

# This function solves the sudoku puzzle by using the backtracking algorithim
def solve(bo):

	row, col = get_empty_slot(bo)
	
	if(row == None and col == None):
		return True
	
	for i in range(1,10):
		is_valid = check_valid(bo, row, col, i)
			
		if (is_valid == True):
			bo[row][col] = i
				
			if solve(bo):
				return True
			
			bo[row][col] = 0

	return False

print("-- Unsolved Sudoku Board -- \n")
print_board(board)

print("\n\n -- Solved Sudoku Board --\n")
solve(board)
print_board(board)

