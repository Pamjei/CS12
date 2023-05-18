#THIS ONE FUCKING WORKS
def differentiate(fxn):
    import re
    ans = "1"
    tokenized = re.findall(r"[\w']+|[()^*-]", fxn)
    trig = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']

    if tokenized[0] == '(':
        tokenized.insert(0,1)
        
    end = next(i for i in reversed(range(len(tokenized))) if tokenized[i] == ')')
    start = tokenized.index('(')

    if tokenized[0] in trig:
        if tokenized[0] == 'cos':
            ans = f'(-sin{"".join(tokenized[1:])})'
        elif tokenized[0] == 'sin':
            ans = f'(cos{"".join(tokenized[1:])})'
        elif tokenized[0] == 'tan':
            ans = f'(sec{"".join(tokenized[1:])}^2)'
        elif tokenized[0] == 'sec':
            ans = f'(sec{"".join(tokenized[1:])}tan{"".join(tokenized[1:])})'
        elif tokenized[0] == 'csc':
            ans = f'(-csc{"".join(tokenized[1:])}cot{"".join(tokenized[1:])})'
        elif tokenized[0] == 'cot':
            ans = f'(-csc{"".join(tokenized[1:])}^2)'
        fxn = f'{"".join(tokenized[1:])}'
        
    elif end == len(tokenized)-1:
        fxn = f'{"".join(tokenized[start+1:end])}'
            
    elif tokenized[end+1] == "^":
        coeff = f'{int(tokenized[end+2])*int(tokenized[0])}'
        exp = int(tokenized[end+2]) - 1
        if exp == 1:
            ans = f'{coeff}{"".join(tokenized[1:-2])}'
        else:
            ans = f'{coeff}{"".join(tokenized[1:-2])}^{exp}'
        fxn = f'{"".join(tokenized[start+1:end])}'
        
    if fxn == 'x':
        return f'{ans}'
    
    else:
        fin = f'{ans}*{differentiate(fxn)}' #might not be necessary
        if fin[0] == '1' and fin[1] == '*':
            return fin[2:]
        elif fin[-1] == '1' and fin[-2] == '*':
            return fin[:-2]
        else:
            return fin
    
fxn = str(input())
print(differentiate(fxn))

#try na number of parenthesis yung pang recurse??
#{outer} * {paloob}
#base case ba paren??
