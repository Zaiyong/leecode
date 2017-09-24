class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos=0-0j
        operation={'U':0+1j,'D':0-1j,'L':-1+0j,'R':1+0j}
        for s in moves:
            pos=pos+operation[s]
        return pos==0-0j
        
