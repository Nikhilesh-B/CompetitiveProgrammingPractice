class Solution:
    def isAnagram(self, s):
        stack = []
        for char in s: 
            stack.append(char)

        new_string = ''
        while len(stack):
            new_string+=stack.pop()
            
        return new_string == s



    def partition(self, s: str) -> list[list[str]]:
        if len(s) == 1:
            return [[s]]        
        partitions = {(i,i+1):[[char]] for i, char in enumerate(s)}
        explored = set()
        
        for length in range(2, len(s)+1):
            print(length)
            for start_idx in range(0,len(s)-length+1):
                end_idx = start_idx+length
                section = s[start_idx:end_idx]
                if self.isAnagram(section):
                    partitions[(start_idx, end_idx)] = [[section]]

                for split in range(start_idx+1, end_idx):
                    part1 = (start_idx, split)
                    part2 = (split, end_idx)
                    if part1 in partitions and part2 in partitions:
                        if (start_idx, end_idx) in partitions:
                            for comb1 in partitions[part1]:
                                for comb2 in partitions[part2]:
                                    if tuple(comb1+comb2) not in explored:
                                        partitions[(start_idx, end_idx)] += [comb1+comb2]
                                        explored.add(tuple(comb1+comb2))

                        else:
                            for comb1 in partitions[part1]:
                                for comb2 in partitions[part2]:
                                    if (start_idx, end_idx) in partitions:
                                        if tuple(comb1+comb2) not in explored:
                                            partitions[(start_idx, end_idx)] += [comb1+comb2]
                                            explored.add(tuple(comb1+comb2))
                                    else:
                                        if tuple(comb1+comb2) not in explored:
                                            partitions[(start_idx, end_idx)] = [comb1+comb2]
                                            explored.add(tuple(comb1+comb2))

        print(partitions)
        return partitions[(0, len(s))]


if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    ans = sol.partition(s)
    print(ans)
    seen = set()
    for seq in ans: 
        seq = tuple(seq)
        if seq in seen:
            print("SCREAM")
        else:
            seen.add(seq)
    
    print("GOOD")


