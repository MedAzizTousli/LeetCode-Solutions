class Solution:
    def __init__(self):
        self.res = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = defaultdict(int)
        mp = defaultdict(list)
        cnt = defaultdict(int)

        for i in tickets:
            mp[i[0]].append(i[1])
            cnt[i[1]] += 1
        for i in mp:
            mp[i].sort(reverse=True)
        cnt["JFK"] += 1
        visited = set()
        print(cnt)
        print(mp)
        print(visited)
        def dfs(curr):
            # if curr in visited:
            #     return
            # visited[curr] += 1
            # visited.add(curr)
            st = mp[curr]
            while st != []:
                visit = st.pop()
                dfs(visit)
            self.res.append(curr)
            # for i in mp[curr]:
            #     dfs(i)
            # visited.remove(curr)
            # visited[curr] -= 1

        dfs("JFK")
        return reversed(self.res)