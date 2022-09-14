# Program makes a simple calculator

# Define add function
def add(x, y):
    return x + y


# Define subtract function
def subtract(x, y):
    return x - y


# Define multiply function
def multiply(x, y):
    return x * y


# Define division function
def divide(x, y):
    return x / y


# Define modulo function
def mod(x, y):
    return x % y

# Displays the options provided by the calculator
print('Select operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Modulo')

use_last = 'N'

while True:
    # Prompts the user to make a choice for an operation and to enter two inputs
    choice = input('Enter choice (1/2/3/4/5): ')
    if use_last == 'Y':
        num1 = last
        num2 = float(input('Enter number: '))
    else:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

    if choice in ['1', '2', '3', '4', '5']:
        if choice == '1':
            last = add(num1, num2)
            print(last)
        elif choice == '2':
            last = subtract(num1, num2)
            print(last)
        elif choice == '3':
            last = multiply(num1, num2)
            print(last)
        elif choice == '4':
            last = divide(num1, num2)
            print(last)
        else:
            last = mod(num1, num2)
            print(last)
    else:
        print('Invalid Input!')

    another = input('Would you like another calculation? (Y/N) ')
    if another == 'N':
        break

    use_last = input('Would you like to use your last calculation as an input? (Y/N) ')


