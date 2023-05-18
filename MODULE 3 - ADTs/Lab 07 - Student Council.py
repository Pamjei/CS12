#strategy: gawing dict yung voter_name para ma-count (?)
#AC WA AC WA BAKET
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
results = {'pres':[],'vp':[],'sec':[],'mc':[],'prc':[],'swc':[],'sr':[]}
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
cnt_pres = Counter()
for vote in pres:
    if vote in candidates: #count lang if present
        cnt_pres[vote] += 1 #count vote per name
results['pres'] = sorted(cnt_pres.items(), key=lambda temp: (-temp[1], temp[0])) #code to arrange dict
if len(results['pres']) > 0 and results['pres'][0][0] not in winners:
    winners.add(results['pres'][0][0]) #name
    print('pres' + ' ' + results['pres'][0][0])
    valid = True
if not valid:
    print('pres ')

valid = False
cnt_vp = Counter()
for vote in vp:
    if vote in candidates:
        cnt_vp[vote] += 1
results['vp'] = sorted(cnt_vp.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(results['vp'])):
    if results['vp'][i][0] not in winners:
        winners.add(results['vp'][i][0])
        print('vp' + ' ' + results['vp'][i][0])
        valid = True
        break
if not valid:
    print('vp ')
    
valid = False
cnt_sec = Counter()
for vote in sec:
    if vote in candidates:
        cnt_sec[vote] += 1
results['sec'] = sorted(cnt_sec.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(results['sec'])):
    if results['sec'][i][0] not in winners:
        winners.add(results['sec'][i][0])
        print('sec' + ' ' + results['sec'][i][0])
        valid = True
        break
if not valid:
    print('sec ')

valid = False
cnt_mc = Counter()
for vote in mc:
    if vote in candidates:
        cnt_mc[vote] += 1
results['mc'] = sorted(cnt_mc.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(results['mc'])):
    if results['mc'][i][0] not in winners:
        winners.add(results['mc'][i][0])
        print('mc' + ' ' + results['mc'][i][0])
        valid = True
        break
if not valid:
    print('mc ')
    
valid = False
cnt_prc = Counter()
for vote in prc:
    if vote in candidates:
        cnt_prc[vote] += 1
results['prc'] = sorted(cnt_prc.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(results['prc'])):
    if results['prc'][i][0] not in winners:
        winners.add(results['prc'][i][0])
        print('prc' + ' ' + results['prc'][i][0])
        valid = True
        break
if not valid:
    print('prc ')

valid = False
cnt_swc = Counter()
for vote in swc:
    if vote in candidates:
        cnt_swc[vote] += 1
results['swc'] = sorted(cnt_swc.items(), key=lambda temp: (-temp[1], temp[0]))
for i in range(len(results['swc'])):
    if results['swc'][i][0] not in winners:
        winners.add(results['swc'][i][0])
        print('swc' + ' ' + results['swc'][i][0])
        valid = True
        break
if not valid:
    print('swc ')

valid = False
cnt_sr = Counter()
for vote in sr:
    if vote in candidates:
        cnt_sr[vote] += 1
results['sr'] = sorted(cnt_sr.items(), key=lambda temp: (-temp[1], temp[0]))
sr_win = []
c = 0
for i in range(len(results['sr'])):
    if results['sr'][i][0] not in winners and c<3:
        winners.add(results['sr'][i][0])
        sr_win.append(results['sr'][i][0])
        valid = True
    c = c+1
if not valid:
    print('sr ')
else:
    print("sr " + " ".join(str(k) for k in sr_win))
#if not valid:
#    print('sr ')
#possible tle, try na diretso na lang sa results yung winner
