'''
use bucket's key to save the numbers of topics they can answer and value to represent 
the number of ways to form the team.
'''
#!/bin/python3

import sys

def numTopic(p1, p2, m):
    result = 0
    for i in range(m):
        if (int(p1[i]) + int(p2[i])) >= 1:
            result += 1
    return result

def acmTeam(topic, n, m):
    bucket = {}
    for i in range(n):
        for j in range(i, n):
            temp_key = str(numTopic(topic[i], topic[j], m))
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


