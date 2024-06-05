def process_case(n, m, og_nums, new_nums, pos_mods):
    #check that necessary changes are available in pos_mods 
    cond1 = True
    required_changes = {}

    og_set = set(og_nums)
    new_set = set(new_nums)

    for i in range(n):
        if og_nums[i] != new_nums[i]:
            if new_nums[i] not in required_changes:
                required_changes[new_nums[i]] = 1
            else:
                required_changes[new_nums[i]] += 1
        
    potential_changes = {}
    necessary_changes = []
    for i in range(m):
        if pos_mods[i] not in potential_changes:
            potential_changes[pos_mods[i]] = 1
        else:
            potential_changes[pos_mods[i]] += 1

    for key in required_changes:
        if key in potential_changes:
            if required_changes[key] > potential_changes[key]:
                cond1 = False
                return
            else:
                necessary_changes+=[key*required_changes[key]]
        else:
            cond1 = False
            return
    
    leftover_changes = potential_changes.copy()

    for change in necessary_changes:
        if change in leftover_changes:
            leftover_changes[change] -= required_changes[change]
            if leftover_changes[change] == 0:
                del leftover_changes[change]


    cond2 = False
    for change in leftover_changes:
        if change in og_set:
            cond2 = True 
            break
        elif change in new_set:
            del leftover_changes[change]
    
    if not leftover_changes:
        cond2 = True

    if cond1 and cond2:
        print("YES")
    
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    n_s, a_s, b_s, m_s, d_s = {}, {}, {}, {}, {}

    for i in range(t):
        n_s[i] = int(input())
        a_s[i] = list(map(int, input().split()))
        b_s[i] = list(map(int, input().split()))
        m_s[i] = int(input())
        d_s[i] = list(map(int, input().split()))

    for i in range(t):
        #number in str
        n = n_s[i]
        #modifications to be made
        m = m_s[i]
        og_nums = a_s[i]
        new_nums = b_s[i]
        pos_mods= d_s[i]
        process_case(n, m, og_nums, new_nums, pos_mods)