class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_list=list(ransomNote)
        m_list=list(magazine)
        for l in r_list:
            try:
                m_list.remove(l)
            except ValueError:
                return False
        return True