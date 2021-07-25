class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        answer = ""

        for i in s:
            if len(answer) < 1:
                stack.append(1)
                answer += i

            elif i == answer[-1]:
                # print(answer[-1], i)
                # print(answer, "before removal")
                if stack and stack[-1] + 1 == k:
                    answer = answer[:-k+1]
                    # print(answer)
                    stack.pop()
                else:
                    answer += i
                    stack[-1] += 1
            else:
                stack.append(1)
                answer += i

        return answer
