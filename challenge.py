"""
This python file contains the code necessary to complete the challenge.
"""
import math


def main():
    """
    Main function call for stdin and stdout.
    """
    inputs = []
    # # Save on that 'big O':
    # running_mean = float()
    # running_sd = float()
    # running_median = float()

    while True:
        user_input = input("Enter a number ('q' to quit): ")
        if user_input == "q":
            break
        try:
            inputs.append(float(user_input))
            print(f"""
            Mean: {mean(inputs)}
            Standard Deviation: {stdev(inputs)}
            Median: {median(inputs)}
            """)
        except (ValueError, TypeError):
            return "Enter an int or float."


# Could use statistics but we'll just code it ¯\_( ͡❛ ͜ʖ ͡❛)_/¯
def mean(data):
    return sum(data) / len(data)


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


def median(data):
    """
    - data is array-like
    """
    sorted_data = sorted(data)
    data_len = len(data)
    index = (data_len - 1) // 2

    if (data_len % 2):
        return sorted_data[index]
    else:
        return (sorted_data[index] + sorted_data[index + 1]) / 2.0


if __name__ == "__main__":
    main()
