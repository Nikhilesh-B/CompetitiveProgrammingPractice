class Solution:
    def generate_perms(self, zeros, ones):
        q = [[]]
        perms = []
        while len(q):
            perm = q.pop(0)
            if len(perm) == zeros+ones:
                perms.append(perm)
            else:
                one_possible = int(len([n for n in perm if n==1])<ones)
                zero_possible = int(len([n for n in perm if n==0])<zeros)
                additions = [[1]]*(one_possible)+[[0]]*(zero_possible)
                for addition in additions:
                    q.append(perm+addition)

        return perms

    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subsets = []
        for zeros in range(n+1):
            perms = self.generate_perms(zeros, n-zeros)
            subsets += [[nums[i] for i, selected in enumerate(perm) if selected==1] for perm in perms]

        return subsets

if __name__ == "__main__":
    s = Solution()
    length = 5 #random.randint(1,10)
    nums = [i for i in range(length)]
    print("Numbers=", nums)
    subsets = s.subsets(nums=nums)
    print(*subsets, sep='\n')
