#list version tc4 na lang
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

def solve(blanks,nums,sudoku):
    for y,x in blanks:
        for n in nums:
            if possible(sudoku,y,x,n):
                sudoku[y][x] = n
                break
    if any('0' in sublist for sublist in sudoku):
        return 'fail'
    else:
        return sudoku
            
T = int(input())
for i in range(T):
    nums = ['1','2','3','4','5','6','7','8','9']
    sudoku = []
    blanks = [] #format: (row y,column x)
    cont = ""
    for y in range(9):
        row = list(input())
        check = "+".join(row)
        for k in row:
            if k in nums and row.count(k)>1:
                cont = 0
                break
        if len(row)>9: #invalid row
            cont = 0
            break
        else:
            if '0' in row:
                if row.count('0') == 1: #check if only single blank
                    new = str(45 - eval(check))
                    old = row.index('0') #palitan na agad yung 0 ng missing
                    row[old] = new
                else:
                    for x in range(9): #if not single blank, list blanks
                        if row[x] == '0':
                            blanks.append((y,x))
            sudoku.append(row)
    if cont == 0:
        print('Could not complete this grid.')
    else:
        ans = solve(blanks,nums,sudoku)
        if ans == 'fail':
            print('Could not complete this grid.')
        else:
            for row in sudoku:
                print(''.join(row))
