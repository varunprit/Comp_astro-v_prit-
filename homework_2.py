import numpy as np
import argparse
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t**2)


def main():
    parser = argparse.ArgumentParser(
        description="Numerical integration of exp(-t^2)",
        usage="\nTo run this code type:\n  python %(prog)s [lower_limit] [upper_limit] [step_size] [--plot] if you want a graph \n\nExample:\n  python %(prog)s 0 1 0.1 --plot\n\nDefaults if no arguments given:\n  lower_limit = 0\n  upper_limit = 3\n  step_size = 0.1"
    ) #add error message /n is to add a line, %prog is to add the file name
    parser.add_argument("a", type=float, nargs='?', default=0, help="Lower limit of integration (default: 0)") #nargs is to make it use default if user doesnt give an input
    parser.add_argument("b", type=float, nargs='?', default=3, help="Upper limit of integration (default: 3)")
    parser.add_argument("step", type=float, nargs='?', default=0.1, help="Size between each point (default: 0.1)")
    parser.add_argument("--plot", action="store_true", help="Show a plot of the function and its integral") #--plot means its optional
    args = parser.parse_args()

    a = args.a
    b = args.b
    step = args.step

    result = trap(f, a, b, step)
    print(f"Integral of exp(-t^2) from {a} to {b} with step size {step} is approximately: {result:.2f}")
    
    if args.plot:
        # Create points for plotting
        t = np.arange(a, b + step, step)
        y = f(t)
        
        # Calculate integral at each point
        integral_values = []
        for point in t:
            integral_values.append(trap(f, a, point, step))
        
        # Got this part from claude to make it interactive
        print("\nAvailable colors: red, blue, green, black, purple, orange")
        while True:
            color = input("Enter the color for the graph: ").lower().strip()
            if color in ['red', 'blue', 'green', 'black', 'purple', 'orange']:
                break
            print("Invalid color! Please choose from the available colors.")
        
        while True:
            line_style = input("Do you want a solid or dashed line? (solid/dashed): ").lower().strip()
            if line_style in ['solid', 'dashed']:
                break
            print("Please enter either 'solid' or 'dashed'")
        
        # Convert user input to matplotlib format
        line_style_dict = {'solid': '-', 'dashed': '--'}
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(t, integral_values, 
                color=color,  # Use color name directly
                linestyle=line_style_dict[line_style],
                label=f'Integral from {a} to {b}')
        plt.grid(True)
        plt.title(f'Function exp(-t²) and its Integral from {a} to {b}')
        plt.xlabel('x')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

def trap(f, a, b, step):
    if step <= 0:
        raise ValueError("Step size must be positive")
    
    # Handle case where a and b are equal or very close
    if abs(b - a) < step:
        return 0.0
    # to make sure user cant break code by putting in b < a
    if b < a:
        raise ValueError("Upper limit must be greater than or equal to lower limit")
    
    # Calculate number of intervals, ensuring at least 1
    n = max(1, int(abs(b - a) / step))
    deltax = (b - a) / n
    
    # Calculate sum
    mysum = 0
    for k in range(1, n+1):
        mysum += f(a + k * deltax)
    
    # Add endpoint contributions
    fa = f(a)
    fb = f(b)
    return deltax * (0.5 * fa + 0.5 * fb + mysum)

if __name__ == "__main__": # This thing means the code will run in the command line
    main()

