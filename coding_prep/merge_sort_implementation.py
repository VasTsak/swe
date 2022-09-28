def sort(myList: list) -> list:

    if len(myList) > 1:
        mid = len(myList) // 2
        right = myList[:mid]
        left = myList[mid:]
    
        # recursive half for every half
        right = sort(right)
        left = sort(left)

        # initiate indexes to traverse over the lists
        i = j = 0

        # iterator for the main list 
        k = 0

        # compare elements of sublists and prioritize the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = left[j]
                j += 1
            k += 1
        
        # to make sure there are no elements behind
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
    return myList

myList = [54,26,93,17,77,31,44,55,20]
print(myList)
myList = sort(myList)
print(myList)

