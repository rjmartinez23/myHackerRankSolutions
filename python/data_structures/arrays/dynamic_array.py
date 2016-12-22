set_num, query_num = map(int, input().split())
lastAns = 0
a = [[] for i in range(set_num)]
for i in range(query_num):
  operation, x, y = map(int, input().split())
  if operation == 1:
    a[(lastAns ^ x)%2].append(y)
  else:
    b = a[(lastAns ^ x)%2]
    lastAns = b[y%len(b)]
    print(lastAns)
