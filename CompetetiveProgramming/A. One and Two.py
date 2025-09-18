#A. One and Two
import sys

def one_and_two():
  t = int(sys.stdin.readline())
  for _ in range(t):
    n = int(sys.stdin.readline())
    array = sys.stdin.readline().split()
    twocount = 0

    #for i in array faster than count(2) according with judge

    for i in array:
      if i == "2":
        twocount += 1

    if twocount == 0:
      print(1)
      continue

    if twocount %2 == 1:
      print(-1)
      continue

    index = 0
    for i, x in enumerate(array, 1):
      if x == "2":
        index += 1
        if index == (twocount//2):
          print(i)
          break

one_and_two()
