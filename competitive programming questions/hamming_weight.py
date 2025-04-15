class Solution:
    def hammingWeight(self, n: int) -> int:
        if n==0:
            return 0 
        else:
            return 1 + self.hammingWeight(n & (n-1))

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(2147483645))