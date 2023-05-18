#string ver

T = int(input())
for i in range(T):
    nums = ['1','2','3','4','5','6','7','8','9']
    sudoku = []
    blanks = [] #format: (row num,position)
    for i in range(9):
        row = str(input())
        check = "+".join(row)
        if eval(check) != 45 and '0' not in row: #invalid row
            print('Could not complete this grid.')
        else:
            if '0' in row:
                if row.count('0') == 1: #check if only single blank
                    new = str(45 - eval(check))
                    row = row.replace('0', new) #palitan na agad yung 0 ng missing
                else:
                    for x in range(len(row)): #if not single blank, list blanks
                        if row[x] == '0':
                            blanks.append((i,x))
            sudoku.append(row)
    #pano na if nasa iisang row
    
