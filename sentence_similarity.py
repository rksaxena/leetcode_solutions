
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if (len(words1) != len(words2)):
            return False

        pairs = set(["#".join(sorted([pair[0], pair[1]])) for pair in pairs])
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if "#".join(sorted([words1[i], words2[i]])) not in pairs:
                return False

        return True
