def calculate_val(input_string):
    MODULO = 10**9 + 7
    running_sum = 0
    val = 1  # Represents 2^0

    # Iterate over the string in reverse order
    for char in reversed(input_string):
        if char == "O":
            running_sum = (running_sum + val) % MODULO
        val = (val * 2) % MODULO  # Efficiently calculate the next power of 2

    return running_sum


if __name__ == "__main__":
    input_str = input()
    print(calculate_val(input_str))
