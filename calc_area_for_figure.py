#area of a triangle by Heron 
print("Select figure:")
print("1 - triangle")
print("2 - square")
print("3 - circle")
figure=int(input())

if figure == 1: #triangle
  a=int(input("Length of side A:"))
  b=int(input("Length of side B:"))
  c=int(input("Length of side C:"))

  p=(a+b+c)/2
  S=(p*(p-a)*(p-b)*(p-c)) ** 0.5
  print("Figure area is:", S)
elif figure == 2: #square
  a=int(input("Length of side A:"))
  b=int(input("Length of side B:"))
  print("Figure area is: ", a*b)
elif figure == 3: #circle
  pi=3.14
  r=int(input("Radius:"))
  print("Figure area is:",pi*(r**2))
