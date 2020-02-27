import csv



matrix = []
rows = []
empty_pos_list = []
subscribing_functions = []

def notify_subscribers(input_matrix):
    for sub in subscribing_functions:
        sub(input_matrix)
        
def subscribe_to_matrix_changes(func):
    subscribing_functions.append(func)

def print_matrix():
    for x in matrix:
        "".join(str(x))
        print(x)

def fill_game_matrix_from_CSV():

    with open("sudoku.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            list_row = list(row)
            matrix.append(list_row)
            

def set_matrix(input_matrix):
    global matrix
    matrix = input_matrix
    
def get_matrix():
    return matrix
            

def check_if_valid(matrix, pos, digit):
    
    # Checks for fixed x-position 
    for y in range(len(matrix)):

        if matrix[y][pos[1]] == str(digit):

            return False
                
               
    # Checks for fixed y-position
    for x in range(len(matrix)):

        if matrix[pos[0]][x] == str(digit):

            return False
            
    #Check box 1
    if pos[0] in range(0, 3) and pos[1] in range(0, 3):

        
        for x in range(0, 3):
            for y in range(0, 3):
                if matrix[x][y] == str(digit):

                    return False
    #Check box 2             
    elif pos[0] in range(3,6) and pos[1] in range(0, 3):

        
        for x in range(3, 6):
            for y in range(0, 3):
                if matrix[x][y] == str(digit):

                    return False
            
            
    #Check box 3 
    elif pos[0] in range(6,9) and pos[1] in range(0, 3):

        for x in range(6, 9):
            for y in range(0, 3):
                if matrix[x][y] == str(digit):

                    return False
                    
    #Check box 4        
    elif pos[0] in range(0, 3) and pos[1] in range(3, 6):

        for x in range(0, 3):
            for y in range(3, 6):
                if matrix[x][y] == str(digit):

                    return False
                 
    #Check box 5
    elif pos[0] in range(3, 6) and pos[1] in range(3, 6):

        for x in range(3, 6):
            for y in range(3, 6):
                if matrix[x][y] == str(digit):

                    return False
                    
    #Check box 6
    elif pos[0] in range(6, 9) and pos[1] in range(3, 6):

        for x in range(6, 9):
            for y in range(3, 6):
                if matrix[x][y] == str(digit):

                    return False
                    
                    
    #Check box 7
    elif pos[0] in range(0, 3) and pos[1] in range(6, 9):

        for x in range(0, 3):
            for y in range(6, 9):
                if matrix[x][y] == str(digit):
                    
                    return False
                    
    #Check box 8                
    elif pos[0] in range(3, 6) and pos[1] in range(6, 9):

        for x in range(3, 6):
            for y in range(6, 9):
                if matrix[x][y] == str(digit):
                    
                    return False
                    
    #Check box 9                
    elif pos[0] in range(6, 9) and pos[1] in range(6, 9):

        for x in range(6, 9):
            for y in range(6, 9):
                if matrix[x][y] == str(digit):
                    
                    return False               
                    
    return True
            
           
def solve_matrix(matrix):
    empty_pos = find_empty_position(matrix)
    if not empty_pos:
        return True
    

    
    for digit in range(1, 10):

        if check_if_valid(matrix, empty_pos, digit):
            matrix[empty_pos[0]][empty_pos[1]] = str(digit)
            if subscribing_functions:
                notify_subscribers(matrix)


            if solve_matrix(matrix):
                return True
            matrix[empty_pos[0]][empty_pos[1]] = "X"
            if subscribing_functions:
                notify_subscribers(matrix)

        
    return False
            

def find_empty_position(matrix):
    for row in matrix:
        for tile in enumerate(row):
            if tile[1] == "X":
                empty_pos = (matrix.index(row), tile[0])
                return empty_pos

    return None

    

if __name__ == "__main__":
    solve_matrix(matrix)
    print_matrix()

