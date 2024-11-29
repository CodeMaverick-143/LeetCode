class Solution(object):
    def mergeAlternately(self, word1, word2):
        min_length = min(len(word1), len(word2))
        merged_word = ""
        
        for i in range(min_length):
            merged_word += word1[i] + word2[i]
        
        merged_word += word1[min_length:] + word2[min_length:]
        
        return merged_word