import math

def print_list_newline(lst):
    for elem in lst:
        print(elem)

def solve():
    x, n = map(int, input().split())
    
    gcd_mx = 1
    
    for k in range(1, int(math.sqrt(x)) + 1):
        if x % k == 0:
            fact1 = k
            fact2 = x // k
            if x // fact1 >= n:
                gcd_mx = max(gcd_mx, fact1)
            if x // fact2 >= n:
                gcd_mx = max(gcd_mx, fact2)
    
    return gcd_mx

def main():
    t = int(input())
    
    answers = []
    
    for _ in range(t):
        answers.append(solve())
    
    print_list_newline(answers)

if __name__ == "__main__":
    main()