from operator import itemgetter
N,L = input().split()
N = int(N)
L = int(L)
Rex_list,Rex_cumm,Rex_fin = [],[],[]
y,z = 0,0
for i in range(N*L):
    Rex = list(input().split())
    Rex_list.append(Rex)
Rex_list.sort()
for x in range(len(Rex_list)):
    if Rex_list[x][2] == "sec":
        Rex_list[x][3] = int(Rex_list[x][3])
    elif Rex_list[x][2] == "min_sec":
        Rex_list[x][3] = list(Rex_list[x][3].split(":"))
        Rex_list[x][3] = int(Rex_list[x][3][0])*60 + int(Rex_list[x][3][1])
    elif Rex_list[x][2] == "hour_min_sec":
        Rex_list[x][3] = list(Rex_list[x][3].split(":"))
        Rex_list[x][3] = int(Rex_list[x][3][0])*60 + int(Rex_list[x][3][1])*60 + int(Rex_list[x][3][2])
while y < (N*L)-1:
    cumm = []
    if Rex_list[y][0] == Rex_list[y+1][0]:
        cumm.append(Rex_list[y][0])
        cumm.append(Rex_list[y][3] + Rex_list[y+1][3])
        Rex_cumm.append(cumm)
    y = y+1
Rex_cumm.sort(key = itemgetter(1))
print(Rex_cumm)
while z < 3:
    H = Rex_cumm[z][1]//3600
    M = (Rex_cumm[z][1]%3600)//60
    S = (Rex_cumm[z][1]%3600)%60
    Rex_cumm[z][1] = str(H) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2)
    print(" ".join(str(x) for x in Rex_cumm[z]))
    z = z+1
