class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        import pdb; pdb.set_trace()
        if len(triangle) == 1:
            return triangle[0][0]

        level = len(triangle) - 2
        while level >= 0:
            for i in range(level+1):
                triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])

        return triangle[0][0]

if __name__ == "__main__":
    triangle = [[1],[2,3]]
    print(Solution().minimumTotal(triangle))
