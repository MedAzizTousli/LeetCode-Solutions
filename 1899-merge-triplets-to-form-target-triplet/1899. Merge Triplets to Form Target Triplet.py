class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        con1 = con2 = con3 = False
        for i, j, k in triplets:
            if i == x and j <= y and k <= z:
                con1 = True
            if i <= x and j == y and k <= z:
                con2 = True
            if i <= x and j <= y and k == z:
                con3 = True
        return con1 and con2 and con3
