class Solution():
    def longestValidParentheses(self, s):
        pstk = []
        mx_length, cur_count = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                pstk.append(c)
            else:
                if pstk:
                    pstk.pop()
                    cur_count += 2
                    mx_length = max(mx_length, cur_count)
                else:
                    pstk = []
                    cur_count = 0
            print(pstk)
        return mx_length


if __name__ == "__main__":
    sol = Solution()
    s = "((((())))(()()()))))()"
    print(sol.longestValidParentheses(s=s))
