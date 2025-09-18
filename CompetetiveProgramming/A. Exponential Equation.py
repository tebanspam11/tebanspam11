#A. Exponential Equation
import sys

def exponential():
  t = int(sys.stdin.readline())
  for _ in range(t):
    n = int(sys.stdin.readline())
    if n %2 == 0:
      print(1, n//2)
      break
    else:
      print(-1)
      break

exponential()

#Observations: Even and odd
