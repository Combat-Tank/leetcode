class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        i = 0
        word_Iref = 0
        padding = 0
        # s size might change with the swaps
        n = len(s)

        while(s[i] == ' '):
            padding += 1
            i += 1
        
        word_Iref = i

        while(i < n):
            if(s[i] == ' ' or i+1 == n):
                aux_idx = i - 1
                if i+1 == n:
                    aux_idx = i

                while word_Iref < aux_idx+padding:
                    if(s[aux_idx] == ' '):
                        aux_idx -= 1
                    s[word_Iref-padding],s[aux_idx] = s[aux_idx],s[word_Iref-padding]
                    word_Iref += 1
                    aux_idx -= 1

                word_Iref = i + 1

            while word_Iref != n and s[word_Iref] ==  ' ':
                padding += 1
                word_Iref += 1
                i = word_Iref - 1

            i += 1

        s = "".join(s)
        s = s.rstrip()
        s = s[::-1]
        print("".join(s))
        return "".join(s)

if __name__ == "__main__":
    Solution.reverseWords(Solution, "ABC  DEFG ")
    Solution.reverseWords(Solution, "  ABC  ")
    Solution.reverseWords(Solution, "A   BC")
    #Solution.reverseWords(Solution, "  Bob    Loves  Alice   ")