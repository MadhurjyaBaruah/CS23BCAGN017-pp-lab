

#program to implementation of function

# Basic function definition
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

# Function with default parameter
def greet(name="World"):
    """Return a greeting message"""
    return f"Hello, {name}!"

# Function that performs calculation
def calculate_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    return area

# Function that processes a list
def find_max(numbers):
    """Find the maximum value in a list"""
    if not numbers:
        return None
    return max(numbers)

# Main function to demonstrate the functions
def main():
    # Using the add function
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    # Using the greet function
    print(greet())
    print(greet("Python"))
    
    # Using the calculate_area function
    area = calculate_area(4, 6)
    print(f"The area of a 4×6 rectangle is {area}")
    
    # Using the find_max function
    numbers = [12, 7, 30, 15, 22]
    maximum = find_max(numbers)
    print(f"The maximum number in {numbers} is {maximum}")

# Run the main function
if __name__ == "__main__":
    main()