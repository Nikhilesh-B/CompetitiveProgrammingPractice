import numpy as np

def array_manipulation(n, queries):
    buffer = [0 for _ in range(n)]

    for q in queries:
        first_idx = q[0]
        second_idx = q[1]
        k = q[2]
        for i in range(first_idx-1,second_idx-1):
            buffer[i] += k
    
    return max(buffer)




if __name__ == '__main__':
    n = 10
    queries = [[1,5,3],[4,8,7],[6,9,1]]
    ans = array_manipulation(n=n,queries=queries)
    print(ans)


























