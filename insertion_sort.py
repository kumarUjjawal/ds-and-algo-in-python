# insertion sort

def insertion_sort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        position = i-1
        while position >= 0 and key < arr[position] : 
                arr[position + 1] = arr[position] 
                position -= 1
        arr[position + 1] = key 

nlist = [5,2,4,6,1,3]
insertion_sort(nlist)
for i in range(len(nlist)):
	print(nlist[i])
