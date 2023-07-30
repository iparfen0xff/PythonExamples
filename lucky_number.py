# Lucky number or Usual
n=input()

left=int(n[0]) + int(n[1]) + int(n[2])
righ=int(n[3]) + int(n[4]) + int(n[5])

if left == righ:
  print("Lucky")
else:
  print("Usual")
