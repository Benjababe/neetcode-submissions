class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        out = [0] * len(temperatures)

        for j, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                _, i = st.pop()
                out[i] = j-i
            
            st.append((temp, j))

        return out