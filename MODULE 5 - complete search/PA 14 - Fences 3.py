#IT WOOOORKSSSSS
T = int(input())
for i in range(T):
    R,C = input().split()
    grid = []
    coordinates = set()
    count = 0
    for i in range(int(R)):
        entry = list(input())
        grid.append(entry)
    #print(grid)
    for y in range(int(R)-2):
        for x in range(int(C)-2):
            if grid[y][x]== "*":
                for i in range(x+2,int(C)):
                    if grid[y][i] == "*":
                        for j in range(2,int(R)):
                            if y+j < int(R):
                                if grid[y+j][x] == "*" and grid[y+j][i] == "*":
                                    coordinates.add(((y,x),(y,i),(y+j,x),(y+j,i)))
                            else:
                                break
    print(len(coordinates))
