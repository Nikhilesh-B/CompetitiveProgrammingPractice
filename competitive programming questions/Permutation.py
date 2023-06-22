class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums)==1:
            return[nums]

        q = [[n] for n in nums]
        rarr = []
        while q:
            print(q)
            n = q.pop(0)
            neighs = [t for t in nums if t not in n]
            for neigh in neighs:
                if len(n)+1 == len(nums):
                    rarr.append(n+[neigh])
                else:
                    q.append(n+[neigh])


        return rarr
    

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    ans = s.permute(nums=nums)
    print(ans)