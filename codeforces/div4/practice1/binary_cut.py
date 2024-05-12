if __name__ == "__main__":
    t = int(input())
    binary_strings = []
    for _ in range(t):
        a = input()
        binary_strings.append(a)

    print(binary_strings)
    for binary_string in binary_strings:
        pieces = 1
        zero_one = False
        for i in range(1, len(binary_string)):
            binary_strings
            if binary_string[i] > binary_string[i-1]:
                if zero_one:
                    pieces += 1
                else:
                    zero_one = True
            elif binary_string[i] < binary_string[i-1]:
                pieces += 1
        print(pieces)
