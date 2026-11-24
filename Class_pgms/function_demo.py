def process_data(data_list):
    subset = data_list[1:4]
    subset[0] = 99
    data_list.append(subset[0])
    return data_list

values = [10, 20, 30, 40, 50]
res = process_data(values)
print(values)