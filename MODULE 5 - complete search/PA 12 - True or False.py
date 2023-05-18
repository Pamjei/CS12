N = int(input())
for i in range(N):
  test = str(input())
  for j in range(64):
    row = []
    bit = bin(j)[2:].zfill(6)
    for k in bit:
      if k == "0":
        row.append(False)
      elif k == "1":
        row.append(True)
    u = row[0]
    v = row[1]
    w = row[2]
    x = row[3]
    y = row[4]
    z = row[5]
    a = str(eval(test.lower()))
    row.append(a)
    print(" ".join(str(x).upper() for x in row))
