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
        flag = 0
        n = n_s[i]
        a = a_s[i]
        b = b_s[i]
        m = m_s[i]
        d = d_s[i]
        
        og_str_set = set(a) 
        new_str_set = set(b)
        diff_in_chars = {}
        for i in range(n):
            if a[i] != b[i]:
                if b[i] not in diff_in_chars:
                    diff_in_chars[b[i]] = 1
                else:
                    diff_in_chars[b[i]] += 1
        
        avail_difs = {}
        for j in range(m):
            if d[j] not in avail_difs:
                avail_difs[d[j]] = 1
            else:
                avail_difs[d[j]] += 1

        
        excess_ok = False

        for key in avail_difs:
            if key in og_str_set:
                excess_ok = True
                break

        for key in avail_difs:
                if key in diff_in_chars: 
                    if avail_difs[key] < diff_in_chars[key]:
                        flag = 1
                        break
                elif key in og_str_set:
                    continue
                elif key not in og_str_set:
                    if excess_ok == False:
                        flag = 1
                        break

        if flag == 1:
            print("NO")
            continue
            
        for key in diff_in_chars:
            if key not in avail_difs:
                flag = 1 
                break
            
        if flag == 1:
            print("NO")
        else:
            print("YES")