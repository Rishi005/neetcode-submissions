class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicts = [{} for _ in range(len(strs))]
        out = {0: [strs[0]]} # key = first idx of dicts/strs from  where it came from, valu3e = grouped list

        for i, string in enumerate(strs):
            for char in string:
                if char not in dicts[i]:
                    dicts[i][char] = 0
                dicts[i][char] += 1
        
        anagram_found = False
        for i, dic in enumerate(dicts[1:]):
            # somehow find match between dic and first element of the values of out?
            for key, value in out.items():
                if dic == dicts[key]:
                    out[key].append(strs[i+1])
                    anagram_found = True
            if not anagram_found:
                out[i+1] = [strs[i+1]]
            anagram_found = False

        #print(list(out.values()))
        return list(out.values())
