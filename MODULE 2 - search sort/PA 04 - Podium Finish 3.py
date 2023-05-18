#matic add agad
from operator import itemgetter
N,L = input().split()
N = int(N)
L = int(L)
Rex_list,Rex_cumm = [],[]
y,z = 0,0
for i in range(N*L):
    Rex = list(input().split())
    if Rex[2] == "sec":
        Rex[3] = int(Rex[3])
    elif Rex[2] == "min_sec":
        Rex[3] = list(Rex[3].split(":"))
        Rex[3] = int(Rex[3][0])*60 + int(Rex[3][1])
    elif Rex[2] == "hour_min_sec":
        Rex[3] = list(Rex[3].split(":"))
        Rex[3] = int(Rex[3][0])*60 + int(Rex[3][1])*60 + int(Rex[3][2])
    del Rex[1]
    del Rex[1]
    if Rex[0] == Rex_list
        Rex[1] + Rex_list[
    Rex_list.append(Rex)
Rex_list.sort()
for index,(name,time) in Rex_list:
    if
    
Rex_cumm.sort(key = itemgetter(1)) #ascending by cumm laps
while z < 3: #makes top 3 in hrs
    H = Rex_cumm[z][1]//3600
    M = (Rex_cumm[z][1]%3600)//60
    S = (Rex_cumm[z][1]%3600)%60
    Rex_cumm[z][1] = str(H) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2)
    print(" ".join(str(x) for x in Rex_cumm[z]))
    z = z+1
#pano pag mas maraming laps
#tle
#OPTIMIZE
#Test1: N10 L5
#Test2: N1000 L8
#no need to check if same kasi magkakasunod agad
