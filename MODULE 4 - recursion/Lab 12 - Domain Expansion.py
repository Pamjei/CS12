def expand(S):
    S.replace("(","")
    S.replace(")","")
    if S == "":
        return ""
    else:
        if S[0].isalpha():
            ans = str(S[0])*int(S[1])
        else:
            ans = ""
        S = S[1:]

        return "".join(str(y) for y in sorted([x for x in (expand(S) + ans)]))

N = int(input())
for i in range(N):
    S = str(input())
    print(expand(S))
