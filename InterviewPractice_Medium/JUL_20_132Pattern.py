class Solution:
    def find132pattern_oN2(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sec = nums[i]
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    if nums[j] < sec:
                        return True
                    elif nums[j] > sec:
                        sec = nums[j]

    # 344ms
    def find132pattern_v2_monotonic_stack(self, nums: List[int]) -> bool:
        stack = []
        s3 = -sys.maxsize

        for i in range(len(nums)-1, -1, -1):
            if s3 > nums[i]:
                return True

            while (stack and stack[-1] < nums[i]):
                s3 = stack.pop()

            stack.append(nums[i])

    # sample 808ms stn.

    def find132pattern_multiple(self, nums: List[int]) -> bool:
        N = len(nums)

        """
        BST
        (PriorityQueue should also work)
        """
        # stack = SortedList()
        # candidate = float('-Inf')
        # for i in reversed(range(N)):
        #     if candidate > nums[i]:
        #         return True
        #     while stack and -stack[-1] < nums[i]:
        #         candidate = max(candidate, -stack.pop())
        #     stack.add(-nums[i])
        # return False

        """
        BST
        
        """
        stack = SortedList()
        candidate = None
        for i in reversed(range(N)):
            if candidate and candidate > nums[i]:
                return True

            while stack and -stack[-1] < nums[i]:
                candidate = -stack.pop()
            stack.add(-nums[i])
        return False

        """
        monotonic stack
        """
        # stack = []
        # candidate = None
        # for i in reversed(range(N)):
        #     if candidate and candidate > nums[i]:
        #         return True
        #
        #     while stack and stack[-1] < nums[i]:
        #         candidate = stack.pop()
        #     stack.append(nums[i])
        # return False

        """
        not work,
        因為必須要是  '132', 這邊 '132', '312' 都會 true
        e.g., [1,0,1,-4,-3]
        """
        # candidates = set()
        # stack = []
        # for i in range(N):
        #     while stack and nums[stack[-1]] <= nums[i]:
        #         stack.pop()
        #     if stack:
        #         candidates.add(i)
        #     stack.append(i)
        #
        # if not candidates:
        #     return False
        #
        # stack = []
        # for i in range(N):
        #     while stack and nums[stack[-1]] >= nums[i]:
        #         stack.pop()
        #     if i in candidates and stack:
        #         return True
        #     stack.append(i)
        #
        # return False
