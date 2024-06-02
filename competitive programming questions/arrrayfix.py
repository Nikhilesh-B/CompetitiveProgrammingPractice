if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        str_arr = input()
        arr = str_arr.split()

        for i in range(len(arr)-1):
            num0 = arr[i]
            num1 = arr[i+1]
            if int(num0) > int(num1):
                if len(num0) == 2:
                    char0 = num0[0]
                    char1 = num0[1]
                    if int(char0) <= int(char1) and int(char1) <= int(num1):
                        continue
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                continue
        print("YES")
