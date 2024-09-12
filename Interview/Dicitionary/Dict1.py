from collections import Counter


store1 = {'apple': 50, 'banana': 30}
store2 = {'banana': 25, 'orange': 40}
store3 = {'apple': 10, 'orange': 20, 'grapes': 15}

collected_dict = dict(Counter(store1)+Counter(store2)+Counter(store3))
print(collected_dict)
