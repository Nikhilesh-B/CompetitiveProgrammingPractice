class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        length = len(intervals)
        intervals.sort(key = lambda x:(x[0],x[1]))
        print(intervals)
        new_intervals = []

        i, j = 0, 0 

        print(intervals)
        while i!=length:
            start_val = intervals[i][0]
            end_val = intervals[i][1]
            while j!=length and intervals[j][0] <= end_val:
                if intervals[j][1] > end_val:
                    end_val = intervals[j][1]
                j+=1
            
            new_intervals.append([start_val, end_val])
            i = j
        
        return new_intervals

if __name__ == "__main__":
    sol = Solution()
    intervals =  [[1,3],[0.8,4],[8,10],[15,18],[1,100]] #[[1,4],[1.2,2]]
    ans = sol.merge(intervals=intervals)
    print("Here is the answer", ans)
