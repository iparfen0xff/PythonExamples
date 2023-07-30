# find common integer divider for both

a = int(input())
b = int(input())
n = a

if b < a:
  n = b
  
while n <= a*b:
  if ((n % a) == 0) and ((n % b) == 0):
    print(n)
    n=a*b #break
  n += 1
