

import cmath  # Handles complex numbers

def arithmetic_operations():
    print("\n--- Arithmetic Operations ---")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Division: {a} / {b} = {a / b}")
    else:
        print("Division by zero is not allowed.")

def solve_quadratic():
    print("\n--- Quadratic Equation Solver ---")
    print("For equation ax² + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("This is not a quadratic equation.")
        return

    d = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)

    print("The roots of the equation are:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

# Main program
print("Choose an option:")
print("1. Arithmetic Operations")
print("2. Solve Quadratic Equation")

choice = input("Enter 1 or 2: ")

if choice == "1":
    arithmetic_operations()
elif choice == "2":
    solve_quadratic()
else:
    print("Invalid choice. Please run the program again.")
