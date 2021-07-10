class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 모든 지점을 한번씩 봐야 한다. ->  o(n)
        # 투포인터를 사용해서 좌, 우로부터 비교를 하고
        # 더 길이가 작은 막대를 가르키고있는 포인터를 옮긴다
        # 포인터가 서로 만나면 비교 종료.
        # 비교하면서도 꾸준히 max 값을 update 하여야 한다.
        if not height:
            return 0

        left, right = 0, len(height)-1
        max_vol = 0

        # 이때, 종료 조건: left = right, 즉, 밑의 실행될 코드를 봤을때, 모든 원소를 한번씩 확인했다.
        while(left < right):
            vol = (right - left) * min(height[left], height[right])
            max_vol = max(vol, max_vol)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return(max_vol)
