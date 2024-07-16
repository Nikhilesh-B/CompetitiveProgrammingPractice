def return_b10(num_str):
    return int(num_str, 2)


# Read the number of test cases
t = int(input())

answers = []

for _ in range(t):
    # Read the integer for this test case
    n = int(input())

    if n == 1 or n == 2:
        answers.append((1, [n]))
        continue

    # Get the binary string representation of n (without the '0b' prefix)
    n_str = bin(n)[2:]

    # Find the indices of '1' bits in the binary string
    one_idxs_order = [i for i, b in enumerate(n_str) if b == '1']

    # List to store the generated numbers
    nums = []

    # Generate new numbers by setting each '1' bit to '0' one at a time
    for ignore_idx in one_idxs_order:
        new_bstr = list(n_str)
        new_bstr[ignore_idx] = '0'
        new_num = return_b10(''.join(new_bstr))
        nums.append(new_num)

    # Add the original number to the list
    nums.append(n)

    # Store the result for this test case
    answers.append((len(nums), nums))

# Print the results for all test cases
for k, sequence in answers:
    print(k)
    print(' '.join(map(str, sequence)))
