def sort_array(source_array):
    # Return a sorted array.
    arr=list()
    for i in range(0, len(source_array)):
        if(source_array[i]%2!=0):
            arr.append([source_array[i],i])
    arr.sort()
    count=0
    for i in range(0, len(source_array)):
        if(source_array[i]%2!=0):
            source_array[i]=arr[count][0]
            count+=1

    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))# [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]))# [1, 3, 5, 8, 0])
print(sort_array([]))#[])