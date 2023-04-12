package main

import "sort"

func rankSlice(slice []float64) []int {
    ranks := make([]int, len(slice))
    sortedSlice := make([]float64, len(slice))
    copy(sortedSlice, slice)
    sort.Float64s(sortedSlice)
    for i, v := range slice {
        rank := sort.SearchFloat64s(sortedSlice, v) + 1
        for j, w := range slice {
            if i != j && w == v {
                rank += 1
            }
        }
        ranks[i] = rank
    }
    return ranks
}