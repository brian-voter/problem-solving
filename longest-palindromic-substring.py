class Solution(object):
    def longestPalindrome(self, s):
        """Returns the longest palindromic substring in the string s."""

        def _find_longest_palindrome_from(s, start_index):
            """Returns the longest palindromic substring in the string s 
            where the 'middle' of the palindrome is at start_index."""

            def _find_longest_palindrome_from_lr(s, left, right):
                """Returns the longest palindromic substring in the string s 
                where the left pointer starts from index left and the right 
                pointer starts from the index right, expanding out towards the 
                ends of the string"""

                is_palindrome = False
                while left >= 0 and right < len(s):
                    if (s[left] != s[right]):
                        break
                    else:
                        is_palindrome = True
                        left -= 1
                        right += 1

                return s[left + 1: right] if is_palindrome else ""

            # for odd length palindromes
            pOdd = _find_longest_palindrome_from_lr(s, start_index - 1, start_index + 1)

            # for even length palindromes
            pEven = _find_longest_palindrome_from_lr(s, start_index - 1, start_index)

            return pEven if len(pEven) > len(pOdd) else pOdd

        longest = s[0:1]
        for start_index in range(1, len(s)):
            p = _find_longest_palindrome_from(s, start_index)
            if len(p) > len(longest):
                longest = p
        return longest
