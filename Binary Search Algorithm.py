#Recursive Binary Search Algorithm
def recursive_binary_search(arr, key, start, end):
    #Error Handling
    if start > end:
        print("Key not found")
        return
    
    #Find the middle of the array
    middle = (start + end) // 2
    #Check if middle of array is the key
    if arr[middle] == key:
        print(f"Key found at index {middle}")
    #Check if the middle of array is bigger than the key
    elif arr[middle] > key:
        recursive_binary_search(arr, key, start, middle - 1 )
    #If none of previous are true than check other side of array
    else:
        recursive_binary_search(arr, key, middle + 1, end)

def iterative_binary_search(arr, key, left, right):
    #When left becomes greater than right, key is not found
    while left <= right:
        #Find middle
        middle = int(left + (right - left) // 2)

        #Returns when middle matches key
        if arr[middle] == key:
            return middle
        
        elif arr[middle] > key:
            #Assigns right index to end of left portion and continues
            right = middle - 1
        else:
            #Assigns left index to start of right portion and continues
            left = middle + 1

    #If loop reaches here, key was not found
    return -1

#Driver code
while True:
    #Array we are searching
    search_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    #Weather we want iterative, recursive or to quit
    method = input("What binary search method would you like to use(Recursive, Iterative, or Exit): ")
    #Quits code
    if method.lower() == "exit":
        break
    
    if method.lower() == "iterative" or method.lower() == "recursive":
        #What is the value we are searching for
        search_value = int(input("What is the number you want to search for: "))

        #Calls recursive function
        if method.lower() == "recursive":
            recursive_binary_search(search_array, search_value, 0, len(search_array) - 1)
        
        #Calls iterative function
        elif method.lower() == "iterative":
            #Assigns return value to result
            result = iterative_binary_search(search_array, search_value, 0, len(search_array) - 1)
            #Print statements for different cases of results
            if result != -1:
                print(f"Key found at index {result}")
            else:
                print("Key not found")
    
    else:
        print("Error: Invalid Response")
        continue
    
    
    
