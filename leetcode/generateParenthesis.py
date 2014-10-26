class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = ["()"]
        if n == 1:
            return result

        while True:
            import pdb; pdb.set_trace()

            t = result.pop(0)
            if len(t) == 2*n:
                result.append(t)
                return result
            for tmp in ["()" + t, "(" + t + ")",  t + "()"]:
                if tmp not in result:
                    result.append(tmp)

        return [""]


if __name__ == "__main__":

    print(Solution().generateParenthesis(4))
