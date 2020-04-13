class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2 = Solution.__remove_back_spaces(s)
        t2 = Solution. __remove_back_spaces(t)

        return s2 == t2

    @staticmethod
    def __remove_back_spaces(s):
        s2 = []
        back_space_count = 0
        for c in reversed(s):
            if c == '#':
                back_space_count += 1
            else:
                if back_space_count == 0:
                    s2.append(c)
                back_space_count = max(0, back_space_count-1)

        return str(s2)


sol = Solution()
result = sol.backspaceCompare("ab#c", "ad#c")
print(f'{result}')