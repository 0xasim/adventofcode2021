# 989 is the max coordinate

with open('5s.txt') as f:
  file = f.read()
T = [l.split('->') for l in file.split('\n') if l]
A = list()
for l in T:
  ta = list()
  for se in l:
    ta.append([int(e) for e in se.split(',') if e])
  A.append(ta)

import numpy as np
floor = np.zeros((10**1, 10**1), dtype=int)
for line in A:
  x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
  # one shared axis
  if (xm := x1 == x2) or (ym := y1 == y2):
    if xm:
      lim = sorted([y1, y2])
      for ny in range(lim[0], lim[1] + 1):
        floor[ny][x1] += 1

    elif ym:
      lim = sorted([x1, x2])
      for nx in range(lim[0], lim[1] + 1):
        floor[y1][nx] += 1
  # diagonals
  else:
    mini, maxi = sorted([int(str(x1)+str(y1)), int(str(x2)+str(y2))])
    if (diff := maxi - mini) % 9 == 0 and maxi != mini or mini == 0:
      diff = maxi - mini
      while diff > 0:
        diff = maxi - mini
        ddI = str(int(maxi))
        if len(ddI) < 2: ddI = "0"+ddI
        ddx, ddy = int(ddI[0]), int(ddI[1])
        floor[ddy][ddx] += 1
        maxi -= 9
        diff = maxi - mini


print()
for f in floor:
  for e in f:
    if e: print(e,end='')
    else: print('.', end='')
  print()
print()

tot = 0
for i in floor:
  for j in i:
    if j >= 2:
      tot += 1

print(tot)
