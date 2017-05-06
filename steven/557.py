class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = ''.join(list(self.reverseWord(words[i])))
        return ' '.join(words)
    
    def reverseWord(self, s):
        word = [c for c in s]
        for i in range(len(word)/2):
            word[i], word[len(word) - 1 - i] = word[len(word) - 1 - i], word[i]
        return word

