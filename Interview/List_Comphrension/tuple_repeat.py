test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
k = 4
n = 3
result = [ele for ele in test_list if ele.count(k) == n]
print(result)
