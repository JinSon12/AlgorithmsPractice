# https://aonecode.com/amazon-online-assessment-debugging-questions#cp
def checkPairSumExists(rows: int, cols: int, arr: List[List[int]], sum: int) -> bool:
    localSet = set()
    localSet.add(0)
    for i in range(0, rows):
        for j in range(0, cols):
            if sum - arr[i][0] - arr[i][j] in localSet:
                return True
            else:
                localSet.add(sum)
    return False
