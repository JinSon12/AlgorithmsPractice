"""
잃어버린 괄호 

https://www.acmicpc.net/problem/1541

string

Key Insight: 
- 덧셈부분을 합해서 빼주면 된다! (가장 큰 수를 만들어서 빼주기.)
- 즉, 
- 1+2+3-4+5+6-6-7 인 경우, 덧셈끼리 묶고,
- (1+2+3)-(4+5+6)-6-7
- 뺄셈해주면 된다. 


Runtime :
- split -> O(n)
- for => O(elements that can be separated by - sign)
- while  => O(len of each section of the formula separated by - sign)

- O(n + (for * while))

Mistakes : 
- 첫번째 부분에 대한 덧셈 처리는 하지 않아서 에러. 
"""


def calculateMin(form):
    exp = form.split("-")

    for i in range(len(exp)):
        el = exp[i]

        el = exp[i].split("+")
        temp = 0

        for num in el:
            temp += int(num)

        exp[i] = temp

    res = exp[0]
    for num in range(1, len(exp)):
        res -= exp[num]

    print(res)


inp = input()
if inp:
    calculateMin(inp)
