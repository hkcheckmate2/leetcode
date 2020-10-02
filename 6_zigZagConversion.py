class Solution:
    def convert(self, s: str, numRows: int) -> str:
        line = 0
        direction = 1
        outp = ["" for i in range(numRows)]
        for i in range(len(s)):
            outp[line] += s[i]
            if numRows > 1:
                line += direction
                if line == 0 or line == numRows -1:
                    direction *= -1
        outputStr = ""
        for row in outp:
            outputStr += row

        return outputStr
