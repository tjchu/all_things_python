print("Welcome to THE CALCULATOR. This program is written entirely in Python.")

exit = False
while exit == False:
  while True:
    number_1 = input('Enter your first number: ')
    if not number_1.isdigit():
      print("EH: First number entered should contain digits only! Try again.")
      continue
    break

  while True:
    number_2 = input('Enter your second number: ')
    if not number_2.isdigit():
      print("EH: Second number entered should contain digits only! Try again.")
      continue
    break

  number_1 = int(number_1)
  number_2 = int(number_2)

  while True:
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    if operation == '+':
      print("%d + %d = %d" % (number_1, number_2, (number_1 + number_2)))
      break

    elif operation == '-':
      print("%d - %d = %d" % (number_1, number_2, (number_1 - number_2)))
      break

    elif operation == '*':
      print("%d * %d = %d" % (number_1, number_2, (number_1 * number_2)))
      break

    elif operation == '/':
      print("%d / %d = %d" % (number_1, number_2, (number_1 / number_2)))
      break

    else:
      print("You have not typed a valid operator, please run the program again."                                                                                                                                                                                               )
      continue

  while True:
    exit_prompt = input("Would you like to calculate again? (Y/N)")
    if exit_prompt.upper() == "Y":
      break
    elif exit_prompt.upper() == "N":
      print("Exiting...")
      exit = True
      break
    else:
      print("Improper input. Try again!")
      continue
