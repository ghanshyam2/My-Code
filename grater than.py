def greater_than_itself(arr):
    lists = []

    for i in range(1, len(arr)):
        for j in range(i):

            if arr[j] > arr[i]:
                lists.append(arr[j])
            else:
                lists.append(-1)
    return lists


print(greater_than_itself([1, 2, 1]))
