class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for ch in s:
            if 'a' <= ch <= 'z':          # Append lowercase letter
                result.append(ch)

            elif ch == '*':               # Remove last character
                if result:
                    result.pop()

            elif ch == '#':               # Duplicate the string
                result = result + result

            elif ch == '%':               # Reverse the string
                result.reverse()

        return "".join(result)


if __name__ == '__main__':
    s= Solution()
    out=s.processStr(s="a#b%*")
    print(out)