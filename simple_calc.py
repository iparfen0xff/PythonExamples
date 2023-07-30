#+, -, /, *, mod, pow, div
operand1=float(input())
operand2=float(input())
func=input()

if func == "+":
  print(operand1 + operand2)
elif func == "-":
  print(operand1 - operand2)
elif func == "/":
  if operand2 == 0:
      print("Division by zero!")
  else:
     print(operand1 / operand2)
elif func == "*":
  print(operand1 * operand2)
elif func == "mod":
  if operand2 == 0:
      print("Division by zero!")
  else:
    print(operand1 % operand2)
elif func == "pow":
  print(operand1 ** operand2)
elif func == "div":
  if operand2 == 0:
      print("Division by zero!")
  else:
    print(operand1 // operand2)

