
def differentiate(fxn):
    import re
    ans = "1"
    tokenized = re.findall(r"[\w']+|[()^*-]", fxn)
    trig = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']
        
    if fxn[0] == '(':
        fxn = '1' + fxn
    
    end = fxn.rfind(')')
    start = fxn.find('(')
    
    if tokenized[0] in trig:
        if tokenized[0] == 'cos':
            ans = f'(-sin{fxn[3:]})'
        elif tokenized[0] == 'sin':
            ans = f'(cos{fxn[3:]})'
        elif tokenized[0] == 'tan':
            ans = f'(sec{fxn[3:]}^2)'
        elif tokenized[0] == 'sec':
            ans = f'(sec{fxn[3:]}tan{fxn[3:]})'
        elif tokenized[0] == 'csc':
            ans = f'(-csc{fxn[3:]}cot{fxn[3:]})'
        elif tokenized[0] == 'cot':
            ans = f'(-csc{fxn[3:]}^2)'
        fxn = f'{fxn[3:]}'
            
    elif end == len(fxn)-1:
        if start == 1 and fxn[0] == '1':
            fxn = f'{fxn[start+1:end]}'
        else:
            fxn = f'{fxn}^1'
    elif fxn[end+1] == "^":
        coeff = f'{int(fxn[end+2])*int(fxn[0])}'
        exp = int(fxn[end+2]) - 1
        if exp == 1 or exp == 0:
            ans = f'{coeff}{fxn[1:-2]}'
        else:
            ans = f'{coeff}{fxn[1:-2]}^{exp}'
        fxn = f'{fxn[start+1:end]}'
    if fxn == 'x':
        if ans == "1":
            return f'{int(ans)*int(coeff)}'
        return f'{ans}'
        print(ans)
    else:
        fin = f'{ans}*{differentiate(fxn)}' #might not be necessary
        if fin[0] == '1' and fin[1] == '*':
            return fin[2:]
        elif fin[-1] == '1' and fin[-2] == '*':
            return fin[:-2]
        else:
            return f'{coeff}{fin}'
    
fxn = str(input())
print(differentiate(fxn))

#try na number of parenthesis yung pang recurse??
#{outer} * {paloob}
#base case ba paren??
