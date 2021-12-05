# 989 is the max coordinate

with open('5.txt') as f:
  file = f.read()
T = [l.split('->') for l in file.split('\n') if l]
A = list()
for l in T:
  ta = list()
  for se in l:
    ta.append([int(e) for e in se.split(',') if e])
  A.append(ta)

import numpy as np
floor = np.zeros((10**3, 10**3), dtype=int)
for line in A:
  x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
  if (xm := x1 == x2) or (ym := y1 == y2):
    #floor[y1][x1] += 1
    #floor[y2][x2] += 1

    if xm:
      lim = sorted([y1, y2])
      for ny in range(lim[0], lim[1] + 1):
        floor[ny][x1] += 1
        #floor[ny][x2] += 1

    elif ym:
      lim = sorted([x1, x2])
      for nx in range(lim[0], lim[1] + 1):
        floor[y1][nx] += 1
        #floor[y2][nx] += 1


for f in floor:
  print()
#print(A, len(A))

tot = 0
for i in floor:
  for j in i:
    if j >= 2:
      tot += 1

print(tot)
