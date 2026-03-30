class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY"

        encoded_str = ""

        for i, st in enumerate(strs):
            if i != (len(strs) - 1):
                encoded_str += st + "#!#"
            else:
                encoded_str += st
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY":
            return []

        return s.split("#!#")