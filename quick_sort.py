def quick_sort(arr,low,high):
	if low < high:
		q = partition(arr,low,high)
		quick_sort(arr,low,q -1)
		quick_sort(arr,low+1,high)

def partition(arr,low,high):
	pivot = arr[high]
	i = low -1
	for j in range(low,high):
		if arr[j] <= pivot:
			i += 1
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return i + 1

arr = [10,1,4,90,32,56,43]
n = len(arr)
quick_sort(arr,0,n-1)
for i in range(n):
	print(arr[i])