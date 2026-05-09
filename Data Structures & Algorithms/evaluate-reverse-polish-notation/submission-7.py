class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                item2 = stack.pop()
                item1 = stack.pop()
                if i == '/':
                    res = int(float(item1) / float(item2))
                else:
                    res = eval(f"{item1} {i} {item2}")
                stack.append(res)
        return int(stack.pop())