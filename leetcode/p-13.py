class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        sum = 0
        while (index < len(s)):
            if (s[index : index + 2] == "IV"):
                sum += 4
                index += 2
            elif (s[index : index + 2] == "IX"):
                sum += 9
                index += 2
            elif (s[index : index + 2] == "XL"):
                sum += 40
                index += 2
            elif (s[index : index + 2] == "XC"):
                sum += 90
                index += 2
            elif (s[index : index + 2] == "CD"):
                sum += 400
                index += 2
            elif (s[index : index + 2] == "CM"):
                sum += 900
                index += 2
            else:
                c = s[index]
                if (c == "I"):
                    sum += 1
                elif (c == "V"):
                    sum += 5
                elif (c == "X"):
                    sum += 10
                elif (c == "L"):
                    sum += 50
                elif (c == "C"):
                    sum += 100
                elif (c == "D"):
                    sum += 500
                elif (c == "M"):
                    sum += 1000
                
                index += 1
            
        return sum


if __name__ == '__main__':
    s = Solution()
    int = s.romanToInt("MCMXCI")
    print(int)