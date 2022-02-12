class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def threeSumClosest(self, A, B):
        lar = pow(10, 9) + 7
        A.sort()
        for i in range(len(A) - 2):
            n = len(A) - 1
            m = i + 1
            while m < n:
                w = A[i] + A[m]
                w = w + A[n]
                if abs(B - w) <= abs(B - lar):
                    lar = w
                if w <= B:
                    m = m + 1
                    continue
                if w > B:
                    n = n - 1
                    continue
        return lar
