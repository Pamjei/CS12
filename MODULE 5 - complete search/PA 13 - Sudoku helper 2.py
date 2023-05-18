sudoku = [list('481253600'),
list('267948135'),
list('539671284'),
list('654389712'),
list('928714563'),
list('173562849'),
list('742136958'),
list('315897420'),
list('896425300')]
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
blanks = [(0, 7), (0, 8), (8, 7), (8, 8)]

def solve(blanks,nums,sudoku):
    for y,x in blanks:
        for n in nums:
            if possible(sudoku,y,x,n):
                sudoku[y][x] = n
                solve(blanks,nums,sudoku)
    if any('0' in sublist for sublist in sudoku):
        return 'fail'
    else:
        return sudoku
print(solve(blanks,nums,sudoku))
