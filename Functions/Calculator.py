def calculator(a, b, operator):
    if operator == '+':
      return a + b
    elif operator == '-':
      return a - b
    elif operator == '*':
      return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
           return "Error: Division by zero"
    else:
      return "Error: Invalid operator"
a=10
b=2

print(calculator(a, b, '+'))  
print(calculator(a, b, '-')) 
print(calculator(a, b, '*'))  
print(calculator(a, b, '/')) 
print(calculator(a, b, '^'))  







