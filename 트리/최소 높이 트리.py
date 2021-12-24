#310

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leafs = []
        for i in range(n):
            if len(graph[i]) == 1:
                leafs.append(i)

        while n > 2:
            n -= len(leafs)
            new_leafs = []

            for leaf in leafs:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leafs.append(neighbor)

            leafs = new_leafs

        return leafs