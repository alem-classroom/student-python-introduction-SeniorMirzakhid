def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    i = 1
    while i < num:
        arr.append(pow(i,2))
    return arr 
print(insert_squares([1,2,3,4,5],5))