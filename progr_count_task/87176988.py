a=int(input())

if 2<=a%10<=4 and not 12<=a%100<=14:
  b='программиста' 
elif a%10 ==1 and a%100!=11:
  b='программист'
else:
  b='программистов'

print(str(a), b)
