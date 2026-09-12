class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            if op == "+":
                n2, n1 = st.pop(), st.pop()
                n3 = n1 + n2
                st.extend([n1, n2, n3])
            elif op == "D":
                n1 = st.pop()
                n2 = n1 * 2
                st.extend([n1, n2])
            elif op == "C":
                st.pop()
            else:
                st.append(int(op))
        
        return sum(st)