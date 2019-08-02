def linear_search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False

arr,num = [12,34,98,2,56],98
linear_search(arr,num)
