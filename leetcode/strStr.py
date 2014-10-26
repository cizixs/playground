class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return None
        if needle == "":
            return haystack
        result = haystack.find(needle)
        if result < 0:
            return None
        return haystack[result:]

