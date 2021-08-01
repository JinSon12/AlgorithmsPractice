from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev_perm = []
        res = []

        def dfs(elements):
            # 종료조건
            if len(elements) == 0:
                res.append(prev_perm[:])       # 이전까지 탐색했던 조합들을 res 에 추가한다.

            for el in elements:
                next_el = elements[:]       # copy elements
                next_el.remove(el)         # 다음으로 전달될 next_el 에서 현재 원소를 없앤다.

                prev_perm.append(el)
                # 재귀적으로 elements 배열에서 현재 원소 el 을 뺀 배열을 전달하여 재귀적으로 prev_perm 에 원소 추가.
                dfs(next_el)
                # 다음 번의 permutation을 위해 이미 탐색된 원소를 배열에서 삭제.
                prev_perm.pop()

        dfs(nums)

        return res

    def permute_recursive_v2(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs(elements, path, res):
            if not elements:
                res.append(path)

            for i in range(len(elements)):
                dfs(elements[:i] + elements[i+1:], path + [elements[i]], res)

        dfs(nums, path, res)

        return res


stn = Solution()
print(stn.permute_recursive_v2([1, 2, 3]))
