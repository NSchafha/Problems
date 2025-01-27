class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        for sc in s:
            seen.add(sc)
        for tc in t:
            if t not in seen:
                return False
        return True