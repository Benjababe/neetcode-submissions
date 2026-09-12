class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                st.append(st.pop() + st.pop())
            elif t == "-":
                st.append(-st.pop() + st.pop())
            elif t == "*":
                st.append(st.pop() * st.pop())
            elif t == "/":
                n2, n1 = st.pop(), st.pop()
                st.append(int(n1 / n2))
            else:
                st.append(int(t))
        return st[-1]