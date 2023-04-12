package mymap

import "golang.org/x/exp/constraints"

type Element[TKey constraints.Ordered, TValue any] struct {
	Key Tkey
	Value TValue
} 
