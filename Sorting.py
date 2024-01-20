def QuickSort(items,choice,by):
    if len(items) <= 1:
        return items
    else:
        pivot = items.pop()
    less, greater = [], []
    for data in items:
        if int(choice) == 5:
            data[choice] = int(data[choice])
            if by == 1 and data[choice] > int(pivot[choice]):
                greater.append(data)
            elif by == 2 and data[choice] < int(pivot[choice]):
                greater.append(data)
            else:
                less.append(data)
        elif int(choice) == 4:
            data[choice] = float(data[choice])
            if by == 1 and data[choice] > float(pivot[choice]):
                greater.append(data)
            elif by == 2 and data[choice] < float(pivot[choice]):
                greater.append(data)
            else:
                less.append(data)
        else:
            if by == 1 and data[choice] > pivot[choice]:
                greater.append(data)
            elif by == 2 and data[choice] < pivot[choice]:
                greater.append(data)
            else:
                less.append(data)
    return QuickSort(less,choice,by) + [pivot] + QuickSort(greater,choice,by)

def ItemSort(items,columns,choice,sort_by,column_index=0,check =True):
    while True :
        if sort_by == 'ascending':
            sort_by = 1
        elif sort_by == 'descending':
            sort_by = 2
        else:
            continue
        for i in range(len(columns)):
            if columns[i].lower() == choice:
                column_index += i
                check = True
                break
        if check == False:
            return items
        sorted_items = QuickSort(items,column_index,sort_by)
        return sorted_items
    
def CRUDSort(items):
    sorted_items = QuickSort(items,0,1)
    return sorted_items