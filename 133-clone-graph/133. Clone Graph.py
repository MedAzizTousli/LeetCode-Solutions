"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        visited = set()
        st = [node]
        head = True
        build2 = None
        visited.add(node)
        mp = {}
        while st:
            currNode = st.pop()
            # print(st)
            if currNode == None:
                continue
            
            currCopy = mp.get(currNode, Node(currNode.val, []))

            # print(currCopy.val, currNode.val)

            if head:
                build2 = currCopy
                head = False
                mp[currNode] = currCopy

            for neighbor in currNode.neighbors:
                # print(neighbor.val)
                # print("not in visited", neighbor.val)
                if neighbor in visited:
                    currCopy.neighbors.append(mp[neighbor])
                # print("neighbor", neighbor)
                else:
                    neighborCopy = Node(neighbor.val, [])
                    mp[neighbor] = neighborCopy
                    st.append(neighbor)
                    visited.add(neighbor)
                    currCopy.neighbors.append(mp[neighbor])

        # print(type(build2))
        # display(build2)
        # print("----")
        # def display(node):
        #     if node == None:
        #         return
        #     print(node.val)
        #     for i in node.neighbors:
        #         display(i)
        # print(build2.neighbors)
        # return build2.val
        # display(build2)
        return build2
