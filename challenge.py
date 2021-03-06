"""
This python file contains the code necessary to complete the challenge.
"""
import math


def main():
    """
    Main function call for stdin and stdout.
    """
    running = Stats()
    # sd_bias_input = input("Bias or unbias SD calculation?")

    while True:
        user_input = input("Enter a number ('q' to quit): ").replace(" ", "")
        if user_input == "q":
            break
        if user_input != "":
            try:
                running.push(float(user_input))
                print(f"List of Inserted Values: {running.values}")

                print(f"""
                    Mean: {running.mean()}
                    Standard Deviation: {running.standard_deviation()}
                    Median: {running.median()}
                    """)
            except (ValueError, TypeError) as e:
                print("Please enter a valid integer or float.")
                print(f"[ERROR] {e}" + "\n")


# Could use statistics but we'll just code it ¯\_( ͡❛ ͜ʖ ͡❛)_/¯
# This is using running statistics
class Stats:
    """
    For continuous calculation of mean - saves time by not passing
    in the list of values each time.

    Saving that 'big O' using running calculations
    """

    def __init__(self):
        """Running stats attributes with saved values"""
        self.n = 0
        self.old_mean = 0
        self.new_mean = 0
        self.old_sd = 0
        self.new_sd = 0
        self.values = []

    def push(self, x):
        """Adds number to values and updates old/new sd & mean"""
        self.n += 1
        self.values.append(x)

        if self.n == 1:
            self.old_mean = self.new_mean = x
            self.old_sd = 0
        else:
            self.new_mean = self.old_mean + (x - self.old_mean) / self.n
            self.new_sd = self.old_sd + \
                (x - self.old_mean) * (x - self.new_mean)

            self.old_mean = self.new_mean
            self.old_sd = self.new_sd

    def mean(self):
        """
        Return self.new_mean value.

        Accounts for non-existent list.
        """
        return self.new_mean if self.n else 0.0

    def variance(self):
        """
        Calculates variance and return variance value.

        Accounts for single value in list.
        """
        return self.new_sd / self.n if self.n > 1 else 0.0

    def standard_deviation(self):
        """
        Calculates standard deviation from variance.
        """
        return math.sqrt(self.variance())

    def median(self):
        """
        Does not roll but utilizes stored values.
        """
        sorted_data = sorted(self.values)
        data_len = len(self.values)
        index = (data_len - 1) // 2

        if (data_len % 2):
            return sorted_data[index]
        else:
            return (sorted_data[index] + sorted_data[index + 1]) / 2.0


# This is not using running values
def mean(data):
    """
    - data is array like
    """
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
