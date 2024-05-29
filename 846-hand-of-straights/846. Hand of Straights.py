class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mp = defaultdict(int, Counter(hand))
        keys = sorted(mp.keys())
        for i in keys:
            while mp[i] > 0:
                for j in range(i, i+groupSize):
                    if mp[j] <= 0:
                        return False
                    mp[j] -= 1
        return True
