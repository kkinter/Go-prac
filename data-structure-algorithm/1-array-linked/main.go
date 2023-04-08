package main

import "fmt"

type Node[T any] struct {
	next *Node[T]
	val  T
}

func Append[T any](node *Node[T], next *Node[T]) *Node[T] {
	node.next = next
	return next
}

func main() {
	root := &Node[int]{nil, 10}
	node := root
	for i := 0; i < 3; i++ {
		node = Append(node, &Node[int]{nil, (i + 2) * 10})
	}

	for n := root; n != nil; n = n.next {
		fmt.Println("Val: ", n.val)
	}

	node = root.next // 20
	originalNext := node.next // 30
	node = Append(node, &Node[int]{nil, 100})
	node.next = originalNext
	
	for n := root; n != nil; n = n.next {
		fmt.Println("Val: ", n.val)
	}
}