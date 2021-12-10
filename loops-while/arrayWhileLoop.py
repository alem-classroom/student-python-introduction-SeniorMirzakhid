def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    i = 1
    while i < num + 1:
        arr.append(pow(i,2))
        i = i + 1
    return arr 
arr = [1,2,3]
print(insert_squares(arr,5))