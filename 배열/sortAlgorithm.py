array = [3, 7, 6, 9, 12, 34, 22, 56, 10, 78, 99, 2]
print(array)

## 선택정렬

for i in range(len(array)): 
    min_index = i # 최솟값 인덱스 저장
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            min_index = j ## 최솟값을 만날 때마다 저장
    array[i], array[min_index] = array[min_index], array[i] ## 찾은 최솟값이랑 변경 

# print(array)

## 삽입정렬

for i in range(1, len(array)): ## 2번째 요소부터 시작
    for j in range(i, 0, -1): ## i부터 왼쪽으로 한 칸씩 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] ## 작은 값을 발견하면 바꾸기
        else:
            break ## 작은 숫자를 만날때까지 반복

# print(array)

## 버블정렬

for i in range(len(array)-1): ## 마지막 요소는 이미 정렬된 것으로 간주함
    for j in range(0, len(array)-i-1): ## 배열길이 - 비교할 인덱스 - 마지막 요소
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j] 

# print(array)

## 합병정렬

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])

    mergeArr = []

    left = right = 0

    while left < len(leftArr) and right < len(rightArr):
        if leftArr[left] < rightArr[right]:
            mergeArr.append(leftArr[left])
            left += 1
        else:
            mergeArr.append(rightArr[right])
            right += 1
    
    mergeArr += leftArr[left:]
    mergeArr += rightArr[right:]
    return mergeArr

mergeSortArray = mergeSort(array)
print(mergeSortArray)

## 퀵정렬

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)

quickSortArray = quickSort(array)
print(quickSortArray)
