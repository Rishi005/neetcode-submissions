class Solution:

    def encode(self, strs: List[str]) -> str:
        # if strs:
        string = "#-#".join(strs)
        # else:
        #     string = strs
        # print(string)
        # print([] == [""])
        if strs ==[]:
            # print(str(None))
            return str(None)
        return string

    def decode(self, s: str) -> List[str]:
        # if s:
        if s == str(None):
            return []
        l = s.split("#-#")
        # else:
        #     l = s
        return l
