"""
This python file contains the code necessary to complete the challenge.
"""
import math


def main():
    """
    Main function call for stdin and stdout.
    """
    inputs = []
    running_mean = float()
    running_sd = float()
    running_median = float()

    while True:
        user_input = input("Enter a number: ")
        if user_input == "q":
            break
        if isinstance(user_input, (float, int)):
            input.append(user_input)
            print(f"""
                Mean: {}
                Standard Deviation: {}
                Median: {}

                Press 'q' to quit.
            """)
        else:
            print("""
            Please enter a valid int or float value.

            Press 'q' to quit.
            """)


# Could use statistics but we'll just code it ¯\_( ͡❛ ͜ʖ ͡❛)_/¯
def variance(data, ddof=0):
    """
    - data is array-like
    - dddof lets us set the degrees of freedom.
    """
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)


def stdev(data):
    """
    - data is array-like
    -| variance dependence
    """
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


if __name__ == "__main__":
    main()
