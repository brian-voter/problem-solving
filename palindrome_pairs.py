class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> s.palindromePairs(["taco", "cat", "abcd", "dcba", "test"])
        [[0, 1], [2, 3], [3, 2]]
        >>> s.palindromePairs(["abcd","dcba","lls","s","sssll"])
        [[0,1], [1,0], [3,2], [2,4]]
        """

        pairs = []

        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if is_palindrome(words[i], words[j]):
                    pairs += [[i, j]]
                if is_palindrome(words[j], words[i]):
                    pairs += [[j, i]]

        return pairs

def index_strings(s1, s2, i):
    if i in range(0, len(s1)):
        return s1[i]
    else:
        return s2[i - len(s1)]

def is_palindrome(s1, s2):
    """
    Test
    >>> is_palindrome("taco", "cat")
    True
    >>> is_palindrome("abcd", "dcba")
    True
    >>> is_palindrome("a", "a")
    True
    >>> is_palindrome("race", "car")
    True
    >>> is_palindrome("abc", "def")
    False
    """

    left = 0
    right = len(s1) + len(s2) - 1

    while left < right:
        # print(left, right, index_strings(s1, s2, left), index_strings(s1, s2, right))
        if (index_strings(s1, s2, left) != index_strings(s1, s2, right)):
            return False
        left += 1
        right -= 1

    return True
