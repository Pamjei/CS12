sudoku = [list('481253697'),
list('267948135'),
list('539671284'),
list('654389712'),
list('908704563'),
list('173562849'),
list('742136958'),
list('315897426'),
list('896425391')]
nums = ['1','2','3','4','5','6','7','8','9']

def possible(sudoku,y,x,n):
    for i in range(0,9):
        if sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+j] == n:
                return False
    return True

def solve(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == '0':
                for n in nums:
                    if possible(sudoku,y,x,n):
                        sudoku[y][x] = n
    return(sudoku)
    #print(solve(sudoku))

print(solve(sudoku))
