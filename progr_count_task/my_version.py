n=input()
l=len(n)
t=n[l-1]

if (l > 1) and n[len(n)-2] == "1":
  print(n,"программистов")
elif t == "0" or t == "5" or t == "6" or t == "7" or t == "8" or t == "9":
  print(n,"программистов")
elif t == "1":
  print(n,"программист")
elif t == "2" or t == "3" or t == "4":
  print(n,"программиста")
