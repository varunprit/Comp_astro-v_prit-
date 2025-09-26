import numpy as np
import argparse
import matplotlib.pyplot as plt
import astropy.constants as const

def func(x):
    G = const.G.si.value #grav const in m^3/kg/s^2
    m_earth = const.M_earth.si.value #earth mass in kg
    m_moon = 7.348e22 #moon mass in kg
    R = 3.844e8 #distance between earth and moon in m
    omega = 2.662e-6 #angular velocity of moon in rad/s
    return (G*m_earth/(x**2)) - (G*m_moon/((R-x)**2)) - omega**2 * x

def central_diff(func, x): #derivative function
    h = 10**-5 # Ideal for central diff
    return ((func(x+(h/2))-func(x-(h/2)))/h)

def main():
    parser = argparse.ArgumentParser(
        description="Finding L1 point between Earth and Moon using Secant method",
        usage="\nTo run this code type:\n  python %(prog)s [initial_guess] [tolerance] [max_iterations]\n\nExample:\n  python %(prog)s 0.5 1e-6 100\n\nDefaults if no arguments given:\n  initial_guess = 0.5\n  tolerance = 1e-6\n  max_iterations = 100"
    )
    parser.add_argument("--initial_guess", type=float, nargs='?', default=0.5, help="Initial guess for the root (default: 0.5)")
    parser.add_argument("--tolerance", type=float, nargs='?', default=1e-6, help="Tolerance for convergence (default: 1e-6)")
    parser.add_argument("--max_iterations", type=int, nargs='?', default=100, help="Maximum number of iterations (default: 100)")
    args = parser.parse_args()

    x = args.initial_guess
    tol = args.tolerance
    max_iter = args.max_iterations

    its_count = 0
    x2 = x - func(x) / central_diff(func, x)  # Initialize x2 for the first iteration

    while abs(x2 - x) > tol and its_count < max_iter:
        its_count += 1
        x = x2
        if abs(central_diff(func, x)) < 1e-12:
            print("Derivative is (close to) zero. No solution found.")
            return
        x2 = x - func(x) / central_diff(func, x)

    if its_count > max_iter:
        print(f"Did not get a solution after {max_iter} tries")
        return
    return x2

if __name__ == "__main__": # This thing means the code will run in the command line
    result = main()
    if result is not None:
        print(f"L1 point found at x = {result:.2f} meters from Earth")
