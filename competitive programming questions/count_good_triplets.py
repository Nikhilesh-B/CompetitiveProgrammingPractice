from bisect import bisect_left

def binarySearch(data, val):
    lo, hi = 0, len(data) - 1
    best_ind = lo
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if data[mid] < val:
            lo = mid + 1
        elif data[mid] > val:
            hi = mid - 1
        else:
            best_ind = mid
            break
        # check if data[mid] is closer to val than data[best_ind] 
        if data[mid]<data[best_ind]:
            best_ind = mid
    return best_ind



def count_good_triplets(sequence, t):
    good_triples = 0
    sequence.sort()

    highest_possible_num = [] 
    for i  in range(len(sequence)):
        for j in range(i, len(sequence)):
            sm = sequence[i]+sequence[j]
            highest_possible_num.append(t-sm)

    for ns in highest_possible_num:
        good_triples += (binarySearch(data=sequence, val=ns))

    return good_triples



print(count_good_triplets(sequence=[1,2,3,4],t=3))