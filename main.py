from functools import reduce

listnum = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filterListNum = list(filter(lambda x: x % 2 == 1, listnum))
print(filterListNum)
reduceListNum = reduce(lambda x, y: x + y, filterListNum)
print(reduceListNum)
