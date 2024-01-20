def Greedy(items, box=5):
    for item in items:
        item.append(float(item[5])/float(item[4]))
    items.sort(key=lambda x: x[7], reverse=True)
    result, pointer = [], -1
    total_income, capacity, filled_capacity = 0, box, 0
    for item in items:
        if len(result) == 0 or capacity < float(item[4]):
            total_income, capacity, filled_capacity = 0, box, 0
            pointer +=1
        if capacity >= float(item[4]):
            capacity -= float(item[4])
            total_income += float(item[5])
            filled_capacity += float(item[4])
            item.pop()
            result.append(item)
    return result