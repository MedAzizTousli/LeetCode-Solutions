class DetectSquares:

    def __init__(self):
        self.mp = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.mp[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point[0], point[1]
        visited = set()
        res = 0
        for cand in self.mp:
            print("----")
            x, y = cand[0], cand[1]
            if y == y0 and x != x0:
                # cand not in visited:
            # if y == y0:
                cote = abs(x-x0)
                pt1 = (x0, y0-cote)
                pt2 = (x, y-cote)
                if cand in self.mp and pt1 in self.mp and pt2 in self.mp:
                    # and cand not in visited and pt1 not in visited and pt2 not in visited:
                    poss = self.mp[cand] * self.mp[pt1] * self.mp[pt2]
                    visited.add(cand)
                    visited.add(pt1)
                    visited.add(pt2)
                    res += poss
                # print(point, cand, pt1, pt2)
                # print(res)
                pt1 = (x0, y0+cote)
                pt2 = (x, y+cote)
                if cand in self.mp and pt1 in self.mp and pt2 in self.mp:
                    # and cand not in visited and pt1 not in visited and pt2 not in visited:
                    poss = self.mp[cand] * self.mp[pt1] * self.mp[pt2]
                    visited.add(cand)
                    visited.add(pt1)
                    visited.add(pt2)
                    res += poss
                # print(point, cand, pt1, pt2)
                # print(res)
        visited = set()
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)