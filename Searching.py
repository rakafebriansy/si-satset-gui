import csv

def BoyerMoore(keyword, data_list):  
    keyword_length, data_length = len(keyword), len(data_list)
    bad_char_table = {}
    for i in range(keyword_length - 1):
        bad_char_table[keyword[i]] = keyword_length - i - 1
    i = keyword_length - 1
    while i < data_length:
        j = keyword_length - 1
        while j >= 0 and data_list[i].lower() == keyword[j]:
            i -= 1
            j -= 1
        if j == -1:
            return True
        if data_list[i] in bad_char_table:
            i += bad_char_table[data_list[i]]
        else:
            i += keyword_length
    return False

def ItemSearch(items,column_index,keyword):
    founded_items = []
    if keyword.replace(' ','').isalnum() or float(keyword):
        for item in items:
            pattern = item[column_index]
            if BoyerMoore(keyword.lower(), pattern.lower()):
                founded_items.append(item)
        if len(founded_items) < 1:
            return False
    else:
        return False
    return founded_items

def SendSearch(items,kota_awal,kota_akhir,keyword_awal,keyword_akhir):
    founded_items = []
    if keyword_awal.replace(' ','').isalnum() and keyword_akhir.replace(' ','').isalnum():
        for item in items:
            pattern1,pattern2 = item[kota_awal], item[kota_akhir]
            if keyword_awal.lower() == pattern1.lower():
                if keyword_akhir.lower() == pattern2.lower():
                    founded_items.append(item)
    else:
        return False
    if len(founded_items) < 1:
        return False
    return founded_items

def CRUDSearch(sorted_items,region,columns,nama_pengirim,nama_penerima,column_index,new_data):
    result = False
    with open(f'{region}.csv', 'w',newline='') as file:
        write = csv.writer(file)
        write.writerow(columns)
        for item in sorted_items:
            if item[0].lower() == nama_pengirim.lower() and item[1].lower() == nama_penerima.lower():
                item[column_index] = new_data.capitalize()
                result = True
            write.writerow(item)
    return result