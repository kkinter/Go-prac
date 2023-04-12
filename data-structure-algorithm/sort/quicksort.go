package sort

import "golang.org/x/exp/constraints"

// 정렬이 가능하려면, 대소 비교가 가능해야하는데,
// Quick[T any] 가 되면 모든 타입이 올 수가 있어서 대소 비교가 안될 수 있음
func QuickSort[T constraints.Ordered](arr []T) {
	if len(arr) <= 1{
		return
	}
	// 먼저 pivot을 기준 왼쪽에 작은값, 오른쪽에 큰값
	idx := partition(arr)
	QuickSort(arr[:idx])
	QuickSort(arr[idx+1:])
}

func partition[T constraints.Ordered](arr []T) int{
	if len(arr) <= 1{
		return 0
	}
	pivot := arr[0]
	i := 1
	j := len(arr) - 1
	
	for {
		for i < len(arr) && arr[i] <= pivot {
			i++
		}
		for j > 0 && arr[j] > pivot {
			j--
		}
		if i >= j {
			arr[0], arr[i-1] = arr[i-1], arr[0]
			return i-1
		}
		arr[i], arr[j] = arr[j], arr[i]
	}
}

func IsSorted[T constraints.Ordered](arr []T) bool{
	if len(arr) <= 1{
		return true
	}
	for i := 1; i < len(arr); i++{
		if arr[i-1] > arr[i]{
			return false
		}
	}
	return true
}