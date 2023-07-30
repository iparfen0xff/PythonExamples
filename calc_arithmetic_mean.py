#find the arithmetic mean (a;b]
# that is divided by 3 without a remainder

# example
# input:
# -5
# 12
#
# output:
# 4.5

a = int(input())
b = int(input())
s = 0
d = 0

for i in range(a, b+1):
  if i % 3 == 0:
    s += i
    d += 1

print(s/d)

