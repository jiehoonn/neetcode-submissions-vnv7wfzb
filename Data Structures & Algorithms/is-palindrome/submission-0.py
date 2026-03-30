class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 65 - 122; 48-57
        new_str = ""

        for char in s:
            if ((48 <= ord(char) <= 57) or
                (65 <= ord(char) <= 122)
            ):
                new_str += char
        
        print(new_str)
        return new_str.lower() == new_str.lower()[::-1]