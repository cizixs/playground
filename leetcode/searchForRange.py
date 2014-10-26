class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A)-1
        low,high = 0,0

        import pdb; pdb.set_trace()
        while start <= end:
            middle = (start + end) / 2
            if A[middle] == target:
                low,high = middle,middle
                while low >= 0 and A[low] == target:
                    low -= 1
                while high < len(A) and A[high] == target:
                    high += 1
                return [low+1, high-1]
            elif A[middle] < target:
                start = middle+1
            else:
                end = middle-1

        return [-1,-1]

if __name__ == "__main__":
    A = [1]
    target = 1
    print(Solution().searchRange(A, target))
