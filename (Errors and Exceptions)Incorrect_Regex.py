import re
for _ in range(int(input())):
    try:
        ans = True
        rep = re.compile(input())
    except re.error:
        ans = False
    print(ans)
