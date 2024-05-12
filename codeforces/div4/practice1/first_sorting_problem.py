if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        numbers = list(map(int, input().split()))
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        print(str(numbers[0]) + " " + str(numbers[1]))
