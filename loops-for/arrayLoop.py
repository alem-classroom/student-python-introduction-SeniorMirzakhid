def insert_squares(arr, num):
    for i in range(1,num + 1):
        arr.append(pow(i,2))
    return arr
arr = [1,2,3]
print(insert_squares(arr,5))

