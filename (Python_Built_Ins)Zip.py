N, X = input().split()
result = []
for _ in range(int(X)):
    temp_score = list(map(float, input().split()))
    result.append(temp_score)
for each_student in zip(*result):
    print(sum(each_student)/len(each_student))
