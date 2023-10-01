def add (x, y):
  return x + y

def subract (x, y):
  return x - y

def multiply (x, y):
  return x * y

def divide (x, y):
  return x / y

def operator_selection():
  print ("Choose operator:")
  print ("1: Add")
  print ("2: Subract")
  print ("3: Multiply")
  print ("4: Divide")
  operator = int(input())
  if operator != 1 and operator != 2 and operator != 3 and operator != 4:
    print ("Invalid operation. Try again")
    operator_selection()
  else:
    return operator
  
def num_input():
  number = input()
  if number.isdigit() == False:
    print ("Invalid number. Insert digits only")
  else:
    return int(number)

def calculation():

  print ("Input first number:")
  num1 = num_input()
  print ("Input second number:")
  num2 = num_input()

  operator = operator_selection()
  print ("Your result is", end = " ")
  if operator == 1:
    result = add (num1, num2)
    print (result)
  elif operator == 2:
    result = subract (num1, num2)
    print (result)

  elif operator == 3:
    result = multiply (num1, num2)
    print (result)

  elif operator == 4:
    result = divide (num1, num2)
    print (result)

  print ("Perform another calculation?")
  print ("Y: Yes")
  print ("N: No")

  decision = input()

  if decision == 'Y' or 'y':
    calculation()
  elif decision == 'N' or 'n':
    print ("Thank you for using this calculator")  
  else:
    print ("Invalid answer")

calculation()




