def is_valid_binary(binary_str):
    """Check if the input string is a valid binary number."""
    return all(char in '01' for char in binary_str)

def binary_to_decimal(binary_str):
    """Convert a binary string to its decimal equivalent."""
    decimal_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        decimal_value += int(digit) * (2 ** i)
    return decimal_value

def main():
    print("Welcome to Bin2Dec!")
    binary_input = input("Enter up to 8 binary digits (0s and 1s): ").strip()

    if len(binary_input) > 8:
        print("Error: Input exceeds 8 binary digits.")
        return

    if not is_valid_binary(binary_input):
        print("Error: Input contains invalid characters. Only 0s and 1s are allowed.")
        return

    decimal_output = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of {binary_input} is {decimal_output}.")

if __name__ == "__main__":
    main()
