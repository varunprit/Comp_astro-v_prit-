import numpy as np
import argparse

def f(t):
    return np.exp(-t**2)


def main():
    parser = argparse.ArgumentParser(description="Integrate exp(-t^2) from a to b using the trapezoidal rule.")
    parser.add_argument("a", type=float, help="Lower limit of integration")
    parser.add_argument("b", type=float, help="Upper limit of integration")
    parser.add_argument("--step", type=float, default=0.1, help="Step size for the trapezoidal rule (default: 0.1)")
    args = parser.parse_args()

    a = args.a
    b = args.b
    step = args.step

    result = trap(f, a, b, step)
    print(f"Integral of exp(-t^2) from {a} to {b} with step size {step} is approximately: {result:.2f}")

def trap(f, a, b, step):
    n = int((b - a) / step)
    deltax=(b-a)/n
    mysum=0
    for k in range(1,n+1):
        mysum+=f(a+k*deltax)
    fa=f(a)
    fb=f(b)
    return deltax*(0.5*fa+0.5*fb+mysum)

if __name__ == "__main__": # This thing means the code will run in the command line
    main()

