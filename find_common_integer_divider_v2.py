# find common integer divider for both
# list comprehension

a, b = (int(i) for i in input().split())
#b = int(input())
#a = int(a)
#b = int(b)

n = a

if b < a:
  n = b
  
while n <= a*b:
  if ((n % a) == 0) and ((n % b) == 0):
    print(n)
    n=a*b #break
  n += 1
