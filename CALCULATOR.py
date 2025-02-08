
operator = input("Enter an operator: (+, -, *, /)\n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operator == "+":
  print("Equals: ", round(num1 + num2))

elif operator == "-":
  print("Equals: ", round(num1 - num2))

elif operator == "*":
  print("Equals: ", round(num1 * num2))

elif operator == "/":
  print("Equals: ", round(num1 / num2, 2))  