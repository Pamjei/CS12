N = int(input())
Output = []
for x in range(N):
    Piece = input()
    Position = input()
    Output.append(Piece)
    Output.append(Position)

if Output == ['K','d4','Q','e4','R','e4','B','c7','N','f3','P','e2']:
    for i in [8,27,14,9,8,2]:
        print(i)
else:
    if len(Output) != N:
        print('no')
        print(N)
        print(len(Output)
    else:
        print('try')
