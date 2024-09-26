class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queue_radiant = []
        queue_dire = []
        for idx, char in enumerate(senate):
            if char == 'R':
                queue_radiant.append(idx)
            else:
                queue_dire.append(idx)
        
        i_radiant = 0
        i_dire = 0
        len_radiant = len(queue_radiant)
        len_dire = len(queue_dire)
        while ((i_radiant < len_radiant) and (i_dire < len_dire)):
            r_index = queue_radiant[i_radiant]
            d_index = queue_dire[i_dire]
            if (r_index < d_index):
                queue_radiant.append(r_index + n)
                len_radiant += 1
            else:
                queue_dire.append(d_index + n)
                len_dire += 1
            i_radiant += 1
            i_dire += 1

        return ("Radiant" if i_radiant < len_radiant else "Dire")
