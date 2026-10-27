class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        spell_list1 = []
        for i in range(len(s)):
            spell_list1.append(s[i])        
        spell_list1.sort()

        spell_list2 = []
        for j in range(len(t)):
            spell_list2.append(t[j])
        spell_list2.sort()

        if spell_list1 == spell_list2:
            return True
        return False