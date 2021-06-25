
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 중심부에 있는 node 는 모든 연결된 노드와 짝.
        # 따라서, 반드시 중심노드와 연결된 갯수만큼 배열에 존재할 것.
        # Tip. 다른 노드에도 반복되는 원소가 있다면? -> 답.

        count = len(edges)

        nodeDict = collections.defaultdict(int)

        # O(2n)
        for i in range(len(edges)):
            nodeDict[edges[i][0]] += 1
            nodeDict[edges[i][1]] += 1

        (max(nodeDict, key=nodeDict.get))
        # (max(k for k,v in nodeDict.items()))
        print(max(v for k, v in nodeDict.items()))

        return (max(nodeDict, key=nodeDict.get))
