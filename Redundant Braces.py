class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        s = []
        for q in A:
            if q != ")":
                s.append(q)
                continue
            if (s[len(s) - 1] == "(" or s[len(s) - 2] == "(") and q == ")":
                return 1

            if q == ")" and s[len(s) - 2] != "(":
                while s[-1] != "(":
                    s.pop()
                s.pop()

        return 0