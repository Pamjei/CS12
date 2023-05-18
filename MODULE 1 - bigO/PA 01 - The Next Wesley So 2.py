
N = int(input())
Output = []
for x in range(N):
    Piece = str(input())
    Position = input()
    Position_Column, Position_Row = list(Position)
    if Piece == 'R':
        Output.append(14)
    elif Piece == 'P':
        if Position_Column == 'a' or Position_Column == 'h':
            Output.append(1)
        else:
            Output.append(2)
    elif Piece == 'K':
        if Position == 'a1' or Position == 'a8' or Position == 'h1' or Position == 'h8':
            Output.append(3)
        elif 'a' < Position_Column < 'h' and Position_Row == '1':
            Output.append(5)
        elif 'a' < Position_Column < 'h' and Position_Row == '8':
            Output.append(5)
        elif '1' < Position_Row < '8' and Position_Column == 'h':
            Output.append(5)
        elif '1' < Position_Row < '8' and Position_Column == 'a':
            Output.append(5)
        else:
            Output.append(8)
    elif Piece == 'B':
        if Position_Column == 'a' or Position_Column == 'h' or Position_Row == '1' or Position_Row ==  '8':
            Output.append(7)
        elif Position_Column == 'b' or Position_Column == 'g' or Position_Row == '2' or Position_Row == '7':
            Output.append(9)
        elif Position_Column == 'c' or Position_Column == 'f' or Position_Row == '3' or Position_Row == '6':
            Output.append(11)
        elif Position_Column == 'd' or Position_Column == 'e' or Position_Row == '4' or Position_Row == '5':
            Output.append(13)
    elif Piece == 'Q':
        if Position_Column == 'a' or Position_Column == 'h' or Position_Row == '1' or Position_Row == '8':
            Output.append(21)
        elif Position_Column == 'b' or Position_Column == 'g' or Position_Row == '2' or Position_Row == '7':
            Output.append(23)
        elif Position_Column == 'c' or Position_Column == 'f' or Position_Row == '3' or Position_Row == '6':
            Output.append(25)
        elif Position_Column == 'd' or Position_Column == 'e' or Position_Row == '4' or Position_Row == '5':
            Output.append(27)
    elif Piece == 'N':
        if Position == 'a1' or Position == 'a8' or Position == 'h1' or Position == 'h8':
            Output.append(2)
        elif Position == 'a2' or Position == 'a7' or Position == 'b1' or Position == 'b8' or Position == 'g1' or Position == 'g8' or Position == 'h2' or Position == 'h7':
            Output.append(3)
        elif 'b' < Position_Column < 'g':
            if Position_Row == '1' or Position_Row == '8':
                Output.append(4)
            elif Position_Row == '2' or Position_Row == '7':
                Output.append(6)
            else:
                Output.append(8)
        elif Position_Column == 'a' or Position_Column == 'h':
            if '2' < Position_Row < '7':
                Output.append(4)
        elif Position_Column == 'b' or Position_Column == 'g':
            if '2' < Position_Row < '7':
                Output.append(6)
            elif Position_Row == '2' or Position_Row == '7':
                Output.append(4)
for x in range(N):
    print(Output[x])
