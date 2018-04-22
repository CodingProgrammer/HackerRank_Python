'''
string to binary: int(s, 2)
int to binary: bin(integer)
'''
#!/bin/python3

import sys
def acmTeam(topic, n, m):
    bucket = {}
    for i in range(n):
        for j in range(i, n):
            temp_key = str(bin(int(topic[i], 2) | int(topic[j], 2))[2:]).count('1')
            if temp_key not in bucket:
                bucket[temp_key] = 1
            else:
                bucket[temp_key] += 1
    for each_key in sorted(bucket, key = int, reverse = True):
        print(each_key)
        print(bucket[each_key])
        break
        return 0

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    topic = []
    topic_i = 0
    for topic_i in range(n):
       topic_t = str(input().strip())
       topic.append(topic_t)
    result = acmTeam(topic, n, m)


