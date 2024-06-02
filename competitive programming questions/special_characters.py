def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 1:
            print("NO")
        else:
            print("YES")
            print("AAB"*(n//2))


if __name__ == "__main__":
    main()
