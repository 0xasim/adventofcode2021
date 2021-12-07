# 989 is the max coordinate

import numpy as np

ft, lim = '5.txt', 10**3
ft, lim = '5s.txt', 10**1
floor = np.zeros((lim, lim), dtype=int)
with open(ft) as f:
  file = f.read()
T = [l.split('->') for l in file.split('\n') if l]
A = list()
for l in T:
  ta = list()
  for se in l:
    ta.append([int(e) for e in se.split(',') if e])
  A.append(ta)

for line in A:
  x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
  mini, maxi = sorted([int(str(x1)+str(y1)), int(str(x2)+str(y2))])
  diff = maxi - mini

  # one shared axis
  if (xm := x1 == x2) or (ym := y1 == y2):
    #print((x1, y1), '-', (x2, y2), '=', (x1 - x2, y1 - y2), 'maxmin', (maxi , mini), \
      #"diff:", diff , (diff % 9, (diff % 11)))
    if xm:
      lim = sorted([y1, y2])
      for ny in range(lim[0], lim[1] + 1):
        floor[ny][x1] += 1

    elif ym:
      lim = sorted([x1, x2])
      for nx in range(lim[0], lim[1] + 1):
        floor[y1][nx] += 1

  # diagonals
  elif (x1 - x2) == (y1 - y2):
    if diff % 9 == 0 or diff % 11 == 0:
        print((x1, y1), '-', (x2, y2), '=', (x1 - x2, y1 - y2), 'maxmin', (maxi , mini), \
          "diff:", diff , (diff % 9, (diff % 11)))
        if diff % 9 == 0: wd = 9
        if diff % 11 == 0: wd = 11

        while diff >= 0:
          ddI = str(int(maxi))
          if len(ddI) < 2: ddI = "0"+ddI
          ddx, ddy = int(ddI[0]), int(ddI[1])
          floor[ddy][ddx] += 1
          maxi -= wd
          diff = maxi - mini
    else:
      print((x1, y1), '-', (x2, y2), '=', (x1 - x2, y1 - y2), 'maxmin', (maxi , mini), \
          "diff:", diff , (diff % 9, diff % 11), "ERROR"*3)

if ft == '5s.txt':
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
