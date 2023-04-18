a = [2, 3, 4, 1, 2, 8, 3, 4, 5, 6]

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             tmp = a[i]
#             a[i] = a[j]
#             a[j] = tmp

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = 1
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

def insertion_sort_ot(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

def insertion_sort_ot_ot(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert


