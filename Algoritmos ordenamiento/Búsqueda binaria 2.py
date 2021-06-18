array = [0, 1]#, 21, 33, 45, 45, 61, 71, 72, 73]
target = -1

def binarySearch2(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right)//2
    potencialMatch = array[mid]
    if target == potencialMatch:
        return mid
    elif target < potencialMatch:
        return binarySearch2(array, target, left, mid - 1)
    else:
        return binarySearch2(array, target, mid + 1, right)


def binarySearch3(array, target, left, right):
    print("l--",left,"--r--",right)
    while left <=right:
        mid = (left + right)//2
        print("m--",mid)
        if array[mid]==target:
            return mid
        elif array[mid] < target:
            right = mid - 1
            print("l--",left,"--r--",right)
        else:
            left = mid + 1
            print("l--",left,"--r--",right)
    return -1

if __name__ == "__main__":
    answer = binarySearch3(array, target, 0, len(array) - 1)
    print(answer)