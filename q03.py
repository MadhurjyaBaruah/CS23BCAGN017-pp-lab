


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D

def plot_star(points=5, size=1, color='gold'):
    """Plot a star using parametric equations"""
    # Create figure
    plt.figure(figsize=(8, 8))
    
    # Parameters for the star
    n = points  # number of points in the star
    inner_radius = 0.5 * size
    outer_radius = size
    
    # Generate the points of the star
    theta = np.linspace(0, 2*np.pi, 2*n+1)
    r = np.zeros_like(theta)
    
    # Alternate between inner and outer radius
    r[0::2] = outer_radius
    r[1::2] = inner_radius
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Plot the star
    plt.fill(x, y, color=color, edgecolor='black')
    plt.axis('equal')
    plt.axis('off')
    plt.title(f"{n}-pointed Star")
    plt.show()

def plot_heart():
    """Plot a heart shape using a mathematical formula"""
    plt.figure(figsize=(8, 8))
    
    # Parameter for the heart curve
    t = np.linspace(0, 2*np.pi, 1000)
    
    # Heart curve equations
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    plt.plot(x, y, color='red')
    plt.fill(x, y, 'red', alpha=0.5)
    plt.axis('equal')
    plt.axis('off')
    plt.title("Heart Shape")
    plt.show()

def plot_sine_wave():
    """Plot a colorful sine wave"""
    plt.figure(figsize=(10, 6))
    
    x = np.linspace(0, 4*np.pi, 1000)
    y1 = np.sin(x)
    y2 = np.sin(x + np.pi/4)
    y3 = np.sin(x + np.pi/2)
    
    plt.plot(x, y1, 'r-', label='sin(x)')
    plt.plot(x, y2, 'g-', label='sin(x + π/4)')
    plt.plot(x, y3, 'b-', label='sin(x + π/2)')
    
    plt.grid(True)
    plt.title("Sine Waves with Phase Shifts")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.show()

def plot_spiral():
    """Plot a spiral using polar coordinates"""
    plt.figure(figsize=(8, 8))
    
    # Spiral equation in polar coordinates
    theta = np.linspace(0, 8*np.pi, 1000)
    r = theta * 0.1
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Create a colormap gradient along the spiral
    colors = np.linspace(0, 1, len(theta))
    plt.scatter(x, y, c=colors, cmap='viridis', s=5)
    
    plt.axis('equal')
    plt.title("Archimedean Spiral")
    plt.grid(False)
    plt.show()

def plot_butterfly_curve():
    """Plot a butterfly curve using parametric equations"""
    plt.figure(figsize=(8, 8))
    
    # Butterfly curve equation
    t = np.linspace(0, 12*np.pi, 10000)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
    
    plt.plot(x, y, 'b-', linewidth=1)
    plt.axis('equal')
    plt.axis('off')
    plt.title("Butterfly Curve")
    plt.show()

def plot_3d_function():
    """Plot a 3D mathematical function"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create data points
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # Calculate Z values (using a sinc function)
    R = np.sqrt(X**2 + Y**2) + 0.001  # Avoid division by zero
    Z = np.sin(R) / R
    
    # Plot surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Sinc Function')
    
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    plt.show()

def main():
    print("Mathematical Graphical Representations")
    print("--------------------------------------")
    print("1. Star")
    print("2. Heart")
    print("3. Sine Waves")
    print("4. Spiral")
    print("5. Butterfly Curve")
    print("6. 3D Function")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        points = int(input("Enter number of points for the star (5-12): "))
        plot_star(points=points)
    elif choice == '2':
        plot_heart()
    elif choice == '3':
        plot_sine_wave()
    elif choice == '4':
        plot_spiral()
    elif choice == '5':
        plot_butterfly_curve()
    elif choice == '6':
        plot_3d_function()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

#-----------------------------------------------------------------------

# sine wave
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

"""
#----------------------------------------------------------------------

# star shape
"""import numpy as np
import matplotlib.pyplot as plt

# Parameters for the star
points = 5
r_outer = 1
r_inner = 0.5

# Create points for the star
angles = np.linspace(0, 2 * np.pi, 2 * points + 1)
radii = np.array([r_outer if i % 2 == 0 else r_inner for i in range(len(angles))])

x = radii * np.cos(angles)
y = radii * np.sin(angles)

plt.figure(figsize=(6, 6))
plt.plot(x, y, 'r-', linewidth=2)
plt.fill(x, y, 'gold')
plt.axis('equal')
plt.title("5-pointed Star")
plt.show()
"""
#----------------------------------------------------------------------

# spiral
"""
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 10 * np.pi, 1000)
r = theta

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.title("Spiral")
plt.axis('equal')
plt.show()
"""