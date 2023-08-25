from collections import deque

def process_max_cpu(cpus, k):
    q = deque()
    mins = []

    for i in range(len(cpus)):
        while q and q[0]<i-k+1:
            q.popleft()
        
        while q and cpus[i]<cpus[q[-1]]:
            q.pop()
        q.append(i)
    
        if i >=k-1:
            mins.append(cpus[q[0]])
        print(q,cpus,q)

    return max(mins)


if __name__ == "__main__":
    cpus = [1,3,-1,-3,5,3,6,7]
    k = 3 
    mins = process_max_cpu(cpus=cpus,k=k)
    print(mins)