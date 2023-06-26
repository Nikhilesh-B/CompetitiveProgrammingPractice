class Solution:
    def partition(self, s: str) -> list[list[str]]:
        length = len(s)
        valid_palindromes = {(i,i) for i in range(length)}
        answers = []

        for len_substring in range(2,length+1):
            for start_idx  in range(0,length+1-len_substring):
                substring = s[start_idx:start_idx+len_substring]
                print(substring)
                if self.isPalindrome(substring):
                    valid_palindromes.add((start_idx,start_idx+len_substring))
    
    def isPalindrome(self, q_string):
        return q_string == q_string[::-1]





if __name__ == "__main__":
    s = Solution()
    string = "abba"
    answers = s.partition(s=string)
    print("The answer is =", answers)