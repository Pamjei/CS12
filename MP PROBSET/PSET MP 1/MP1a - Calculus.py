#wala pang trig
def differentiate(fxn):
    import re
    if fxn == '()':
        return 1
    else:
        ans = "1"
        tokenized = re.findall(r"[\w']+|[()^*-]", fxn)
        trig = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']
        
        if fxn[0] == '(':
            fxn = '1' + fxn
            
        end = fxn.rfind(')')
        start = fxn.find('(')

        if end == len(fxn)-1:
            fxn = f'{fxn[start+1:end]}'
        elif fxn[end+1] == "^":
            coeff = f'{int(fxn[end+2])*int(fxn[0])}'
            exp = int(fxn[end+2]) - 1
            if exp == 1:
                ans = f'{coeff}{fxn[1:-2]}'
            else:
                ans = f'{coeff}{fxn[1:-2]}^{exp}'
            fxn = f'{fxn[start+1:end]}'
                
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
