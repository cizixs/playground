class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):

        if not A:
            return 0

        m = max(A)

        if m == 1:
            return 0

        full = m * len(A)

        i,s,level = 0,0,0
        lmax,rmax=-1,-1
        while A[i] < m:
            level = max(level, A[i])
            s += m - level + A[i]
            i += 1
        lmax = i
        s += m

        i = len(A) - 1
        level = 0
        while A[i] < m:
            level = max(level, A[i])
            s += m - level + A[i]
            i -= 1

        rmax = i
        if lmax != rmax:
            s += m
            for i in range(lmax+1, rmax):
                s += A[i]

        return full - s
