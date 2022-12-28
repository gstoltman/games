import numpy as np
import random

#Global Variables

gridsquared = grid * grid
pair_count = int(gridsquared / 2)

print('Select grid size (use 2 for this demo)')
grid = int(input())
print('Grid size of ' + str(grid) + 'x' + str(grid) + ' chosen')

##Initialize Game Board

reveal_list = []
hidden_list = []

for i in range(pair_count):
    reveal_list.append(i+1)

for i in range(pair_count):
    hidden_list.append(0)

reveal_list = reveal_list * 2
shuffle_list = random.sample(reveal_list, len(reveal_list))
hidden_list = hidden_list * 2

hidden_matrix = np.array(hidden_list).reshape(grid, grid)

shuffle_matrix = np.array(shuffle_list).reshape(grid, grid)

print(hidden_matrix)

def pick_cell():
        
    print('Select a column:')
    col_select1 = int(input()) - 1

    print('Select a row:')
    row_select1 = int(input()) - 1
    
    reveal_value1 = shuffle_matrix[row_select1][col_select1]
    
    hidden_matrix[row_select1][col_select1] = reveal_value1

    print(hidden_matrix)

    print('Select a column:')
    col_select2 = int(input()) - 1

    print('Select a row:')
    row_select2 = int(input()) - 1
    
    reveal_value2 = shuffle_matrix[row_select2][col_select2]
    
    hidden_matrix[row_select2][col_select2] = reveal_value2
    
    print(hidden_matrix)
    
    print("Hit any key to confirm")
    input()
    
    if shuffle_matrix[row_select1][col_select1] != shuffle_matrix[row_select2][col_select2]:
        print("No Match")
        hidden_matrix[row_select1][col_select1] = 0
        hidden_matrix[row_select2][col_select2] = 0
    
    print(hidden_matrix)
    
while (0 in hidden_matrix):
    pick_cell()
    
print("You win!")
