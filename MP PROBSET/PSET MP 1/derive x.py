def derive(fxn):
    import re
    if '(x)' not in fxn:
        return "0"
    else:
        tokenized = re.findall(r"[\w']+|[()^*-]", fxn)

        if tokenized[0] == '(':
            tokenized.insert(0,1)
        
        end = next(i for i in reversed(range(len(tokenized))) if tokenized[i] == ')')
        start = tokenized.index('(')

        if end == len(tokenized)-1:
            tokenized.append('^')
            tokenized.append('1')
            
        if tokenized[end+1] == "^":
            coeff = f'{int(tokenized[end+2])*int(tokenized[0])}'
            exp = int(tokenized[end+2]) - 1
            if exp == 1:
                ans = f'{coeff}{"".join(tokenized[1:-2])}'
            elif exp == 0:
                ans = f'{coeff}'
            else:
                ans = f'{coeff}{"".join(tokenized[1:-2])}^{exp}'
        
        return f'{ans}'    
    
fxn = str(input())
print(derive(fxn))
