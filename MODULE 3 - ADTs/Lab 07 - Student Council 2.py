#strategy: gawing dict yung voter_name para ma-count (?)
#POTA AC WA AC WA NAMAN TO
from collections import Counter
from operator import itemgetter
N = int(input())
candidates = set()
winners = set()
pres = []
vp = []
sec = []
mc = []
prc = []
swc = []
sr = []
pres_tally = []
vp_tally = []
sec_tally = []
mc_tally = []
prc_tally = []
sw_tally = []
sr_tally = []

for i in range(N):
    entry = list(input().split())
    candidates.add(entry[0]) #voters as candidates
    if len(entry)!=1:
        for i in range(1,len(entry)-1,2): #enter voted person per category
            if entry[i] == 'pres':
                pres.append(entry[i+1])
            if entry[i] == 'vp':
                vp.append(entry[i+1])
            if entry[i] == 'sec':
                sec.append(entry[i+1])
            if entry[i] == 'mc':
                mc.append(entry[i+1])
            if entry[i] == 'prc':
                prc.append(entry[i+1])
            if entry[i] == 'swc':
                swc.append(entry[i+1])
            if entry[i] == 'sr':
                sr.append(entry[i+1])
valid = False
cnt_pres = Counter(pres)
pres_tally = sorted(cnt_pres.items(), key=lambda temp: (-temp[1], temp[0])) #code to arrange dict
for i in range(len(pres_tally)):
    if pres_tally[i][0] in candidates and pres_tally[i][0] not in winners:
        winners.add(pres_tally[i][0])
        print('pres' + ' ' + pres_tally[i][0])
        valid = True
        break
if not valid:
    print('pres ')

valid = False
cnt_vp = Counter(vp)
vp_tally = sorted(cnt_vp.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(vp_tally)):
    if vp_tally[i][0] in candidates and vp_tally[i][0] not in winners:
        winners.add(vp_tally[i][0])
        print('vp' + ' ' + vp_tally[i][0])
        valid = True
        break
if not valid:
    print('vp ')
    
valid = False
cnt_sec = Counter(sec)
sec_tally = sorted(cnt_sec.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(sec_tally)):
    if sec_tally[i][0] in candidates and sec_tally[i][0] not in winners:
        winners.add(sec_tally[i][0])
        print('sec' + ' ' + sec_tally[i][0])
        valid = True
        break
if not valid:
    print('sec ')

valid = False
cnt_mc = Counter(mc)
mc_tally = sorted(cnt_mc.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(mc_tally)):
    if mc_tally[i][0] in candidates and mc_tally[i][0] not in winners:
        winners.add(mc_tally[i][0])
        print('mc' + ' ' + mc_tally[i][0])
        valid = True
        break
if not valid:
    print('mc ')
    
valid = False
cnt_prc = Counter(prc)
prc_tally = sorted(cnt_prc.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(prc_tally)):
    if prc_tally[i][0] in candidates and prc_tally[i][0] not in winners:
        winners.add(prc_tally[i][0])
        print('prc' + ' ' + prc_tally[i][0])
        valid = True
        break
if not valid:
    print('prc ')

valid = False
cnt_swc = Counter(swc)
swc_tally = sorted(cnt_swc.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(swc_tally)):
    if swc_tally[i][0] in candidates and swc_tally[i][0] not in winners:
        winners.add(swc_tally[i][0])
        print('swc' + ' ' + swc_tally[i][0])
        valid = True
        break
if not valid:
    print('swc ')

valid = False
cnt_sr = Counter(sr)
sr_tally = sorted(cnt_sr.items(), key=lambda temp: (-temp[1], temp[0]))
sr_win = []
c = 0
for i in range(len(sr_tally)):
    if sr_tally[i][0] in candidates and sr_tally[i][0] not in winners and c<3:
        winners.add(sr_tally[i][0])
        sr_win.append(sr_tally[i][0])
        valid = True
    c = c+1
if not valid:
    print('sr ')
else:
    print("sr " + " ".join(str(k) for k in sr_win))
#if not valid:
#    print('sr ')
#possible tle, try na diretso na lang sa results yung winner
