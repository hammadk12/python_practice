import tkinter as tk

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
    
# Function to perform calculation
def perform_calculation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Error: Invalid input")

# Function to clear inputs and result
def clear_all():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="")

# Function to create GUI
def create_gui():
    root = tk.Tk()
    root.title("Simple Calculator")

    global entry_num1, entry_num2, label_result

    entry_num1 = tk.Entry(root)
    entry_num1.grid(row=0, column=1)

    entry_num2 = tk.Entry(root)
    entry_num2.grid(row=1, column=1)

    label_num1 = tk.Label(root, text="Enter number 1:")
    label_num1.grid(row=0, column=0)

    label_num2 = tk.Label(root, text="Enter number 2:")
    label_num2.grid(row=1, column=0)

    button_add = tk.Button(root, text="Add", command=lambda: perform_calculation('add'))
    button_add.grid(row=2, column=0)

    button_subtract = tk.Button(root, text="Subtract", command=lambda: perform_calculation('subtract'))
    button_subtract.grid(row=2, column=1)

    button_multiply = tk.Button(root, text="Multiply", command=lambda: perform_calculation('multiply'))
    button_multiply.grid(row=3, column=0)

    button_divide = tk.Button(root, text="Divide", command=lambda: perform_calculation('divide'))
    button_divide.grid(row=3, column=1)

    button_clear = tk.Button(root, text="Clear", command=clear_all)
    button_clear.grid(row=4, column=0, columnspan=2)

    label_result = tk.Label(root, text="")
    label_result.grid(row=5, column=0, columnspan=2)

    root.mainloop()
    

#Modified main function for GUI integration
def main():
    create_gui()

#this checks if the script is run directly and then calls the function
if __name__ == "__main__":
    main()


    
