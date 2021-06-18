array = [8, 5, 2, 9, 5, 6, 3]

def bubbleSort(array):
    isTrue = False
    mas_ = 0
    while not isTrue:
	    isTrue = True
	    for i  in range(len(array) - 1 - mas_):
		    if array[i] > array[i+1]:
			    array[i] , array[i+1] = array[i+1] , array[i]
			    isTrue = False
		
	    mas_ +=1
	
    return array

if __name__ == "__main__":
     data = bubbleSort(array)
     print(data)