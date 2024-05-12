
def min_length_after_removal(n, s):
    stack = []  # Stack to keep track of characters
    for char in s:
        if stack and stack[-1] != char:
            stack.pop()  # Remove the pair if adjacent characters are different
        else:
            stack.append(char)
    return len(stack)



# Input: Number of test cases
t = int(input())
for _ in range(t):
    # Input: Length of the string and the string itself
    n = int(input())
    s = input()
    
    # Calculate and print the minimum length
    result = min_length_after_removal(n, s)
    print(result)



if __name__ == "__main__":
    pass