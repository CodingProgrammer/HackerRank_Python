'''
Beautiful_Binary_String: string without '010' inside it
Algorithm: Iterate the whole string and find '010', then replace the last '0' with '1'
Fault: '101' still there or reproduced
'''
#!/bin/python3

import sys

def beautifulBinaryString(b):
    # Complete this function
    step = 0
    sub_string = '010'
    for i in range(0, n - 2):
        if b[i: i + 3] == sub_string:
            b = b[0 : i + 2] + '1' +b[i + 3: ]
            step += 1
    return step 
if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)