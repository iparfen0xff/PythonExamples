#2000 - a leap year 
#2100 - NOT a leap year

y=int(input())
if 1900 <= y <= 3000:
  if ((y%4) == 0) and ((y%100) != 0) or ((y%400)==0):
    print("A leap year")
  else:
    print("NOT a leap year")

