package mymap

import (
	"sort"

	"golang.org/x/exp/constraints"
)

type Element[TKey constraints.Ordered, TValue any] struct {
	Key TKey
	Value TValue
} 

type SortedMap[TKey constraints.Ordered, TValue any] struct {
	Arr []Element[TKey, TValue]
}

func (s *SortedMap[TKey, TValue]) Add(key TKey, value TValue) {
	//키 값이 키보다 크거나 같아지는 최소한 인덱스를 찾아서 삽입
	idx := sort.Search(len(s.Arr), func(i int) bool {
		return s.Arr[i].Key >= key
	})
	// sort.Search 는 비어있으면 0을 반환 -> 비어있는 상태 확인 필요

	if idx < len(s.Arr) && s.Arr[idx].Key == key {
		s.Arr[idx].Value = value
		return
	}

	s.Arr = append(s.Arr[:idx], // arr 에서 인덱스 까지 슬라이스 한 부분
		append([]Element[TKey, TValue]{ // 추가하려는 값
			{Key: key, Value:value},
			}, s.Arr[idx:]...)... ) // 인덱스 부터 슬라이스 한 부분
}

func (s *SortedMap[TKey, TValue]) Get(key TKey) (value TValue, ok bool){
	// 아래의 search 는 같다는 보장이 없다
	idx := sort.Search(len(s.Arr), func(i int) bool {
		return s.Arr[i].Key >= key
	})

	if idx < len(s.Arr) && s.Arr[idx].Key == key {
		return s.Arr[idx].Value, true
	}
	// 초기값
	var defaultV TValue
	return defaultV, false
}

func (s *SortedMap[TKey, TValue]) Remove(key TKey) (removed bool){
	// 아래의 search 는 같다는 보장이 없다
	idx := sort.Search(len(s.Arr), func(i int) bool {
		return s.Arr[i].Key >= key
	})

	if idx < len(s.Arr) && s.Arr[idx].Key == key {
		s.Arr = append(s.Arr[:idx],s.Arr[idx+1:]... )

		return true
	}
	return false
}