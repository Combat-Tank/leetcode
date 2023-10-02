class Solution:
    def intToRoman(self, num: int) -> str:
        index = 0
        same_char_count = 0
        roman = []

        value_array_map = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
        
        while num > 0:
            while num < value_array_map[index][1]:
                index += 1
                same_char_count = 0
            num -= value_array_map[index][1]
            roman.append(value_array_map[index][0])
            same_char_count += 1
            if same_char_count > 3:
                for i in range(4):
                    roman.pop()
                if len(roman) != 0:
                #higher than 5, 50, 500 cases; need to remove that character
                    if roman[-1] == value_array_map[index-1][0]:
                        roman.pop()
                        roman.append(value_array_map[index][0])
                        roman.append(value_array_map[index-2][0])
                        same_char_count = 0
                        index += 1
                        continue
                    
                roman.append(value_array_map[index][0])
                roman.append(value_array_map[index-1][0])
                same_char_count = 0
                index += 1
        
        return ''.join(roman)

if __name__ == '__main__':
    Solution.intToRoman(Solution,4)
    Solution.intToRoman(Solution,58)
    Solution.intToRoman(Solution,989)
    Solution.intToRoman(Solution,1994)
            