

def solve_linear_equation(a, b):
    """
    Solves a linear equation of the form 'ax + b = 0'
    
    Parameters:
    a (float): coefficient of x
    b (float): constant term
    
    Returns:
    float: solution for x, or None if no unique solution exists
    """
    if a == 0:
        if b == 0:
            print("Infinite solutions (Every x satisfies the equation)")
        else:
            print("No solution (Equation is inconsistent)")
    else:
        x = -b / a
        print(f"The solution of the linear equation {a}x + {b} = 0 is:")
        print(f"x = {x}")

# user input
a = float(input("Enter coefficient a: "))
b = float(input("Enter constant b: "))
solve_linear_equation(a, b)













#linear equations with two variables in the form: a1x + b1y = c1  and a2x + b2x = c2

"""
def solve_two_variables(a1, b1, c1, a2, b2, c2):
    # Calculate the determinant
    D = a1 * b2 - a2 * b1

    if D == 0:
        # Check if the equations are dependent or inconsistent
        if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print("Infinite solutions (the two equations are the same line).")
        else:
            print("No solution (the lines are parallel).")
    else:
        # Use Cramer's Rule
        Dx = c1 * b2 - c2 * b1
        Dy = a1 * c2 - a2 * c1

        x = Dx / D
        y = Dy / D

        print("Unique solution:")
        print(f"x = {x}")
        print(f"y = {y}")

# Get inputs from user
print("Solving equations of the form:")
print("a1*x + b1*y = c1")
print("a2*x + b2*y = c2\n")

a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))
a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

solve_two_variables(a1, b1, c1, a2, b2, c2)
"""
