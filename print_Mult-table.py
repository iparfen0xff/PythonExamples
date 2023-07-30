#Print table of multiplication, where:
# a - start of range
# b - end of range
# c - start range multiple
# d - end range multiple

# Example
# input:
# 7
# 10
# 5
# 6
#
# output:
#    5   6
# 7  35  42
# 8  40  48
# 9  45  54
# 10 50  60



a = int(input())
b = int(input())
c = int(input())
d = int(input())

#head
for n in range(c,d+1):
  print("\t", n, end="")
print()

#table
for i in range(a,b+1):
  print(i, end="")
  for n in range(c,d+1):
    print("\t", i*n, end="")
  print()

