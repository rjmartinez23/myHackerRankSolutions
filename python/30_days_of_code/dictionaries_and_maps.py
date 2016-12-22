n = int(input())

phone_book = {}

for i in range(0, n):
  data = input().split()
  phone_book[data[0]] = data[1]

for query in range(0, n):
  query = input()
  if query in phone_book:
    print('{}={}'.format(query, phone_book[query]))
  else:
    print('Not found')
