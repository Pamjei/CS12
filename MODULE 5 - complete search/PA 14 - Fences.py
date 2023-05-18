#configure pa yung sa y
T = int(input())
for i in range(T):
    R,C = input().split()
    grid = []
    coordinates = set()
    for i in range(int(R)):
        entry = list(input())
        grid.append(entry)
    #print(grid)
    for y in range(int(R)-2):
        for x in range(int(C)-2):
            if grid[y][x] == "*":
                for i in range(2,int(C)):
                    if x+i < int(C):
                        if grid[y][x+i] == "*" and grid[y+2][x] == "*" and grid[y+2][x+i] == "*":
                            coordinates.add(((y,x),(y,x+i),(y+2,x),(y+2,x+i)))
                    else:
                        break
                for j in range(2,int(R)):
                    if y+j < int(R):
                        if grid[y][x+2] == "*" and grid[y+j][x] == "*" and grid[y+j][x+2] == "*":
                            coordinates.add(((y,x),(y,x+2),(y+j,x),(y+j,x+2)))
                    else:
                        break
    print(len(coordinates))            
    #print(coordinates)
            #coordinates.append([grid[y][x], grid[y][x+i], grid[y+2][x], grid[y+2][x+i]])
            #for j in (2,int(R)-2,2):
                #coordinates.append([grid[y][x], grid[y][x+2], grid[y+j][x], grid[y+j][x+2]]
 
