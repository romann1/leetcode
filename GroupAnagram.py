from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for cur_str in strs:
            sorted_str = str(sorted(cur_str))
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(cur_str)
            else:
                anagram_map[sorted_str] = [cur_str]

        return list(anagram_map.values())


print(f'{Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])}')
