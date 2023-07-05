class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        lets_to_nums = {'2':['a','b','c'],
                        '3':['d','e','f'],
                        '4':['g','h','i'],
                        '5':['j','k','l'],
                        '6':['m','n','o'],
                        '7':['p','q','r','s'],
                        '8':['t','u','v'],
                        '9':['w','x','y','z']}
        letters=[]

        for digit in digits:
            if len(letters) == 0:
                letters = lets_to_nums[digit]
            else:
                new_letters = []
                for let in letters:
                    for char in lets_to_nums[digit]:
                        new_letters.append(let+char)
                
                letters = new_letters
        
        return letters



if __name__ == "__main__":
    sol = Solution()

