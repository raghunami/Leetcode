class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        # seen = [] 
        # w = "" 
        # for ch in s: 
        #     if ch == ' ': 
        #         seen.append(w) 
        #         w = ""
        #     else:
        #         w += ch 

        # if w:
        #     seen.append(w) 
        
        # return " ".join(word for word in seen[::-1] if word.strip())

       
        
            