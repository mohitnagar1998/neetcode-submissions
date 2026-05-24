class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for index in range(len(s)):
            if s[index] != "]":
                stack.append(s[index])
            else:
                subString = ""
                while stack[-1] != "[":
                    subString = stack.pop() + subString
                stack.pop()
                
                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                
                stack.append(int(count) * subString)

        return "".join(stack)