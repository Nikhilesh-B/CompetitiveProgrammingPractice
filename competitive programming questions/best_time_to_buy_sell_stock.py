import math
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pric_idx_list = [(p,i) for i, p in enumerate(prices)]
        pric_idx_list.sort(key=lambda x:(x[0],x[1]))
        print(pric_idx_list)
        i = 0 
        j = len(prices)-1
        mx_price = -math.inf
        while i<j:
            print(i,j)
            p_prev, i_prev = pric_idx_list[i]
            p_next, i_next = pric_idx_list[j]
            if i_next>i_prev:
                mx_price = max(mx_price, p_next-p_prev)
                break
            else:
                p_prev_next, i_prev_next = pric_idx_list[i+1]
                p_next_prev, i_next_prev = pric_idx_list[j-1]
                if i_prev_next<i_next and i_next_prev>i_prev:
                    mx_price = max(mx_price, p_next-p_prev_next,p_next_prev-p_prev)
                    break
                
                elif i_prev_next<i_next:
                    i+=1
                
                elif i_next_prev>i_prev:
                    j-=1
                
                else:
                    i+=1
                    j-=1
        if mx_price<0:
            return 0
        else:
            return mx_price


if __name__ == "__main__":
    s = Solution()
    lst = [4,7,1,2]
    print(s.maxProfit(prices=lst))
