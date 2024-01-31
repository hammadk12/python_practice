# Simple Calculator

#function for addition
def add(x, y):
    return round(x + y, 2)

#function for subtraction
def subtract(x, y):
    return round(x - y, 2)

#function for multiplication
def multiply(x, y):
    return round(x * y, 2)

#function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return round(x/y, 2)

#This defines the main function
def main():
  print("Welcome to the calculator!")

  while True:
    #Initialize num1 and num2 before the try block
    num1 = None
    num2 = None

    while True:
     try:
        #Ask user for input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        break
     except ValueError:
        print("Invalid input. Please enter a number.")
        
    
    #Inner loop for operation choice
    operation = None
    while True:
    #Ask the user to choose an operation
            operation = input("Choose an operation (1. Add, 2. Subtract, 3. Multiply, 4. Divide): ")
            if operation in ['1', '2', '3', '4']:
                break #Valid choice, break out of the inner loop
            else:
                print("Invalid choice. Please enter a valid operation number (1, 2, 3, 4).")
       
    if operation == '1':
            result = add(num1, num2)
    elif operation == '2':
            result = subtract(num1, num2)
    elif operation == '3':
            result = multiply(num1, num2)
    elif operation == '4':
            result = divide(num1, num2)
    else:
            result = "Invalid Input"

    #Print the result
    print("Result: ", result)

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break

#this checks if the script is run directly and then calls the function
if __name__ == "__main__":
    main()


    
