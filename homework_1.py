import math
import argparse

def time(h,g=9.81):  #having g = 9.81 means keyword argument
    t = ((2*h)/g)**0.5
    return t

def main(): #got this from chat GPT but made some edits
    parser = argparse.ArgumentParser(
        description="Calculate the free fall time from a given height."
)
    parser.add_argument(
        "height",
        type=float,
        help="Height (in m) from which the object is dropped."
    )

    args = parser.parse_args()

    t = time(args.height)
    print(f"The time an object would take to fall from a height of {args.height} m on earth is {t:.2f} seconds.")

if __name__ == "__main__": # This thing means the code will run in the command line
    main()