class Solution:
    def gcd(n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1%n2
        return n1
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2+str1 != str1+str2:
            return ""
        n = len(str1)
        m = len(str2)
        g = gcd(n,m)
        return str1[:g]
        