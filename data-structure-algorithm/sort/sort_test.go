package sort

import (
	"math/rand"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestQuickSort(t *testing.T) {
	arr := make([]int, 10)
	for i := 0; i < 10; i++ {
		arr[i] = rand.Intn(100)
	}
	assert.False(t, IsSorted(arr))
	QuickSort(arr)
	assert.True(t, IsSorted(arr))
	// go test -v 
	t.Log(arr)
}
func TestMergeSort(t *testing.T) {
	arr := make([]int, 10)
	for i := 0; i < 10; i++ {
		arr[i] = rand.Intn(100)
	}
	assert.False(t, IsSorted(arr))
	sorted := MergeSort(arr)
	assert.True(t, IsSorted(sorted))
}

func TestInsertSort(t *testing.T) {
		arr := make([]int, 0, 100)
	for i := 0; i < 10; i++ {
		arr = BinaryInsertSort(arr, rand.Intn(100))
	}
	assert.True(t, IsSorted(arr), arr)
}