#list version
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

def solve(nums,sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == '0':
                for n in nums:
                    if possible(sudoku,y,x,n):
                        sudoku[y][x] = n
                        solve(nums,sudoku)
                        sudoku[y][x] = 0
                        
nums = ['1','2','3','4','5','6','7','8','9']
sudoku = []
for i in range(9):
    entry = list(input())
    sudoku.append(entry)

print(solve(nums,sudoku))
