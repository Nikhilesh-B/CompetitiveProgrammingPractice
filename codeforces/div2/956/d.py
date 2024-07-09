t = int(input())


answers = []


def solve(a,b,n):
    if a == b:
        return "YES"
    
    a_copy = a.copy()
    b_copy = b.copy()
    a_copy.sort()
    b_copy.sort()
    if a_copy != b_copy:
        return "NO"

    ## relative distances for different numbers are the same in both arrays in terms of indexes

    
    




for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    answers.append(solve(a, b, n))


for ans in answers:
    print(ans)
