class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def matches(s, p):
            saved_sols = {}

            if p == "" and s == "":
                return True 
            
            else:
                qmark_cnt, str_cnt = 0, 0
                start_idx, end_idx, pattern = -1, -1, None
                for i, char in enumerate(p):
                    if char == "?":
                        qmark_cnt += 1
                    elif char == "*":
                        str_cnt += 1
                    else:
                        start_idx, end_idx = i, i 
                        pattern = char

                        for c in p[i+1:]:
                            if c != "?" and c != "*":
                                pattern += c
                                end_idx += 1
                            else:
                                break

                        break
                
                
                if start_idx == -1:
                    if str_cnt:
                        return len(s) >= qmark_cnt
                    
                    else:
                        return len(s) == qmark_cnt

                else:
                    if pattern not in s:
                        return False

                    dif = end_idx-start_idx
                    saved_s_idxs = []
                    b = False

                    if str_cnt:
                        for j in range(len(s)-dif):
                            if s[j:j+dif+1] == pattern and j>=qmark_cnt:
                                saved_s_idxs.append((j,j+dif))

                    else:
                        for j in range(len(s)-dif):
                            if s[j:j+dif+1] == pattern and j==qmark_cnt:
                                saved_s_idxs.append((j,j+dif))
                                break


                    for idx in saved_s_idxs:
                        sidx, eidx = idx[0], idx[1]
                        b = b or matches(s[eidx+1:],p[end_idx+1:])

                    return b


        while "**" in p:
            idx = p.index("**")
            p = p[:idx+1]+p[idx+2:]
        
        return matches(s, p)




