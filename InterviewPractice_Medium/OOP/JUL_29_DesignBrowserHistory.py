# https://leetcode.com/problems/design-browser-history/


""""
1472. Design Browser History


Key Insight: 
- two stacks solution; history and fwd 
- The history stack never gets emptied, the last element would be the website that the user is currently visiting 
- This is combined with peek (or stack[-1]), to get the current website. 

Source or Error/Difficulty: 
- Issue was handling the visit and the future stack part. 
- When we visit a website, the forward history would be cleared, but it wasn't cleared, and that was yielding incorrect result.
- The current website would already be stored in the history (so there was no need to store it in the future array when we visit.)
"""


# The solution O(steps)
class BrowserHistory:
    #  296 ms, faster than 44.01%
    # 16.8 MB, less than 9.49%
    def __init__(self, homepage: str):
        self.history = []
        self.visit(homepage)
        self.future = []

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        bwd = self.history

        while len(bwd) > 1 and steps > 0:
            res = bwd.pop()
            self.future.append(res)
            steps -= 1

        return bwd[-1]

    def forward(self, steps: int) -> str:
        fwd = self.future

        while fwd and steps > 0:
            res = fwd.pop()
            self.history.append(res)
            steps -= 1

        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# O(1)
class BrowserHistory2:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]
