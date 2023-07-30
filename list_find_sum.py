# calc sum of list elements
# input:
# 4 -1 9 3
#
# output:
# 15

sum = 0

a = [int(i) for i in input().split()]
for i in a:
  sum += i  
print(sum)
