class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        
        if s[0] == 'I':
            value += 1
        elif s[0] == 'V':
            value += 5
        elif s[0] == 'X':
            value += 10
        elif s[0] == 'L':
            value += 50
        elif s[0] == 'C':
            value += 100
        elif s[0] == 'D':
            value += 500
        elif s[0] == 'M':
            value += 1000
        
        index = 1
        while index < len(s):
            if s[index] == 'I':
                value += 1    
            elif s[index] == 'V':
                if s[index-1] == 'I':
                    value -= 2
                value += 5
            elif s[index] == 'X':
                value += 10
                if s[index-1] == 'I':
                    value -= 2
            elif s[index] == 'L':
                value += 50
                if s[index-1] == 'X':
                    value -= 20
            elif s[index] == 'C':
                value += 100
                if s[index-1] == 'X':
                    value -= 20
            elif s[index] == 'D':
                value += 500
                if s[index-1] == 'C':
                    value -= 200
            elif s[index] == 'M':
                value += 1000
                if s[index-1] == 'C':
                    value -= 200
            index += 1
        return value
                
