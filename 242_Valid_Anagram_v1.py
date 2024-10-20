class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s_count = dict()
        dict_t_count = dict()
        for i in s:
            if i not in dict_s_count :
                dict_s_count[i] = 1
            else:
                dict_s_count[i] += 1
        for j in t:
            if j not in dict_t_count :
                dict_t_count[j] = 1
            else:
                dict_t_count[j] += 1

        if len(dict_s_count.keys()) == len(dict_t_count.keys()):
            for x in dict_s_count.keys() :
                if x not in  dict_t_count:
                    return False
                if dict_s_count[x] != dict_t_count[x]:
                    return False
                else:
                    continue
            return True
        else: 
            return False
      
      #time complex : O(n)
      #space complex : O(n)