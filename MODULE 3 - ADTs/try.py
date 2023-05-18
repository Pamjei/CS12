from collections import Counter
pres = ['Slice', 'Mark','Slice','Slice','Mark','Nat']
cnt_pres = Counter(pres)
for x in sorted(cnt_pres.items(), key=lambda temp: (-temp[1], temp[0])):
    print(x)

#for x in sorted(pres, key=lambda jed: (pres[jed]*-1, jed)):
    #print(x)
