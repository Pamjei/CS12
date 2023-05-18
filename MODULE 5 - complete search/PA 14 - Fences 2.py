#configure pa yung sa y
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
            if grid[y][x] == "*":
                for i in range(x,int(C)-2):
                    if grid[y][i] == "*" and grid[y+2][i] == "*" and grid[y+2][x] == "*":
                        coordinates.add(((y,x),(y+2,x),(y,i),(y+2,i)))
                for j in range(y,int(R)-2):
                    if grid[j][x] == "*" and grid[j][x+2] == "*" and grid[y][x+2] == "*":
                        coordinates.add(((y,x),(y+2,x),(y,i),(y+2,i)))
                    
    print(len(coordinates))            
    #print(coordinates)
            #coordinates.add(((y,x),(y,x+i),(y+2,x),(y+2,x+i)))
            #for j in (2,int(R)-2,2):
                #coordinates.append([grid[y][x], grid[y][x+2], grid[y+j][x], grid[y+j][x+2]]
 
