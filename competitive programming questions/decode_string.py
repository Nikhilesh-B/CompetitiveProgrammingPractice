class Solution:
    def decodeString(self, s: str) -> str:
        if "[" not in s:
            return s

        else:
            stack = []
            for idx, char in enumerate(s):
                if char == "[": 
                    if len(stack)==0:
                        number = int(s[idx-1])
                        open_brack_idx = idx
                    stack.append(char)
                
                if char == "]":
                    stack.pop()
                    if len(stack)==0:
                        close_bracket_idx = idx
                        break
            
            return self.decodeString(s[0:open_brack_idx-1]+number*s[open_brack_idx+1:close_bracket_idx]+s[close_bracket_idx+1:]) 



if __name__ =="__main__":
    string = "2[abc]3[cd]ef"
    string_2 = "3[a2[c]]"
    string_3 = "3[a]2[bc]"
    sol = Solution()
    decoded_string = sol.decodeString(s=string_3)

    print("Decoded string =", decoded_string) 

