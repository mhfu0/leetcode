class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d1 = {c: 1 for c in 'qwertyuiop'}
        d2 = {c: 2 for c in 'asdfghjkl'}
        d3 = {c: 3 for c in 'zxcvbnm'}
        d = {}
        d.update(d1)
        d.update(d2)
        d.update(d3)
        
        valid_words = []
        for word in words:
            original_word = word
            word = word.lower()
            if len(word) > 0:
                
                row = d[word[0]]
                for w in word[1:]:
                    if d[w] != row:
                        break
                else:
                    valid_words.append(original_word)
        return valid_words
