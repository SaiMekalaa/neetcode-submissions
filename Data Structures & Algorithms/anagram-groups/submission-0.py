class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for value in strs:
            sorted_value="".join(sorted(value))
            result[sorted_value].append(value)

        return list(result.values())


