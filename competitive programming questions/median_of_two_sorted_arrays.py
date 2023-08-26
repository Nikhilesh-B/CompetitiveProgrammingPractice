class Solution():
    def compute_median(self, sorted_arr):
        length = len(sorted_arr)
        if length%2==0:
            idx1, idx2 = (length-1)//2,((length-1)//2)+1
            return (sorted_arr[idx1]+sorted_arr[idx2])/2

        else:
            return sorted_arr[length//2]

    def manually_merge(self, sarr1, sarr2):
        narr = sarr1+sarr2
        narr.sort()
        return self.compute_median(narr)

    def median_two_sorted_arrays(self, arr1, arr2):
        #base cases; think about all the possible base cases that can occur and allow us to consider them
        
        #work through the computation of the arrays as you see fit 
        m = len(arr1)
        n = len(arr2)
        if m+n<5:
            return self.manually_merge(arr1,arr2)
        
        elif m == 0:
            return 
        
        else: 
            if m%2==0:
                top_arr1 = arr1[m//2-1:]
                bottom_arr1 = arr1[:m//2+1]
                idx1, idx2 = (m-1)//2,(m-1)//2+1
                median_arr1 = self.compute_median(arr1)

            else:
                top_arr1 = arr1[m//2:]
                bottom_arr1 = arr1[:m//2+1]
                median_arr1 = self.compute_median(arr1)

            if n%2==0:
                top_arr2 = arr2[n//2-1:]
                bottom_arr2 = arr2[:n//2+1]
                idx1, idx2 = (n-1)//2,(n-1)//2+1
                median_arr2 = self.compute_median(arr2)
            
            else:
                top_arr2= arr2[n//2:]
                bottom_arr2 = arr2[:n//2+1]
                median_arr2 = self.compute_median(arr2)

            if median_arr1<median_arr2:
                return self.median_two_sorted_arrays(arr1=top_arr1,arr2=bottom_arr2)

            elif median_arr1>median_arr2:
                return self.median_two_sorted_arrays(arr1=bottom_arr1,arr2=top_arr2)
                
            else:
                return median_arr1



if __name__ == "__main__":
    sol = Solution()
    arr1, arr2 = [1,7,9], [2,3,6]
    print(sol.median_two_sorted_arrays(arr1=arr1, arr2=arr2))
