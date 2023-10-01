def add (x, y):
  return x + y

def subract (x, y):
  return x - y

def multiply (x, y):
  return x * y

def divide (x, y):
  return x / y

print ("Input first number")
num1 = int(input())
print ("Input second number")
num2 = int(input())

print ("Choose operator:")
print ("1: Add")
print ("2: Subract")
print ("3: Multiply")
print ("4: Divide")

operation = int(input())
if operation == 1:
  add (num1, num2)
if operation == 2:
  subract (num1, num2)
if operation == 3:
  multiply (num1, num2)
if operation == 4:
  divide (num1, num2)
  
