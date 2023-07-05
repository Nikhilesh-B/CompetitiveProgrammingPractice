class Solution:
    # def trap(self, height: list[int]) -> int:
    #     mx_h = max(height)
    #     width = len(height)
    #     total = 0
    #     left_ref = 0 
    #     right_ref = width-1
    #     for h in range(mx_h+1):
    #         for j in range(left_ref,right_ref):
    #             if height[j] >= h:
    #                 break

    #         for k in range(right_ref,left_ref-1,-1):
    #             if height[k] >= h:
    #                 break

    #         for i in range(j+1,k):
    #             if height[i] < h:
    #                 total += 1 

    #         left_ref = j
    #         right_ref = k

    #     return total

    def find_highest_left(self, heights, i, height):
        for j, height_2 in enumerate(heights[0:i]):
            if height_2 > height:
                return height, j 
        return None, None
        
    def find_highest_right(self, heights, i, height):
        for j in range(len(heights)-1,i,-1):
            height_2 = heights[j]
            if height_2 > height:
                return height, j 
        return None, None
    
    def trap(self, heights:list[int]) -> int:
        width = len(heights)
        total = 0
        hh_left_idx = None
        hh_right_idx = None
        hh_left= None
        hh_right = None
        for i, height in enumerate(heights): 
            if i == 0 or i == width -1:
                continue 

            if hh_left_idx==None:
                hh_left_idx, hh_left = self.find_highest_left(heights, i, height)
            
            if hh_right_idx==None:
                hh_right_idx, hh_right = self.find_highest_right(heights, i, height)
            
            
            
            if not(hh_left_idx==None or hh_right_idx==None):
                min_h = min(hh_left, hh_right)
                if i == hh_right_idx:
                    if hh_left<hh_right:
                        hh_left_idx=i 
                        hh_left = hh_right
                    hh_right_idx = None
                    continue
                if height<min_h:
                    total += min_h-height




        return total


import random
if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    length = 100
    #height = [random.randint(0,int(10**5)) for _ in range(int(2*10**4))]
    #print("mx height=", max(height))
    #print(height)
    ans = s.trap(heights=height)
    print("The answer to the amount of liquid that can be stored inside is", ans)
