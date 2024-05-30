class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(chr, Counter(s))
        print(mp)
        st = set()
        curr = 0
        res = []
        for i in s:
            curr += 1
            mp[i] -= 1
            st.add(i)
            if mp[i] == 0:
                st.remove(i)
            if len(st) == 0:
                res.append(curr)
                curr = 0
        return res