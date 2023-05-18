#IT WOOOORKS!!!
#shet pwede pala dict dito
from operator import itemgetter
N,L = input().split()
N = int(N)
L = int(L)
Rex_list,Rex_cumm = [],[]
y,z = 0,0
for i in range(N*L): #gawing same format lahat
    Rex = list(input().split())
    if Rex[2] == "sec":
        Rex[3] = int(Rex[3])
    elif Rex[2] == "min_sec":
        M , S = map(int, Rex[3].split(':'))
        Rex[3] = S + 60*M
    elif Rex[2] == "hour_min_sec":
        H, M , S = map(int, Rex[3].split(':'))
        Rex[3] = S + 60*(M + 60*H)
    del Rex[1]
    del Rex[1]
    Rex_list.append(Rex)
Rex_list.sort()
for j in range(0,N*L,L):
    entry = []
    entry = [Rex_list[j+k][1] for k in range(L)] #lagay sa isang list yung mga time per name
    Rex_cumm.append([Rex_list[j][0],sum(entry)]) #sum yung times tapos ipartner sa name
Rex_cumm.sort(key = itemgetter(1))
while z < 3: #makes top 3 in hrs #mali ito dahil di inaccount pag days
    H = Rex_cumm[z][1]//3600
    M = (Rex_cumm[z][1]%3600)//60
    S = (Rex_cumm[z][1]%3600)%60
    Rex_cumm[z][1] = str(H) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2)
    print(" ".join(str(k) for k in Rex_cumm[z]))
    z = z+1
#pano pag mas maraming laps
#tle
#OPTIMIZE
#Test1: N10 L5
#Test2: N1000 L8
#no need to check if same kasi magkakasunod agad
