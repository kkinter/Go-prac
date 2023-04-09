package doublelinkedlist

type Node[T any] struct {
	next  *Node[T]
	prev  *Node[T]
	Value T
}

type LinkedList[T any] struct {
	root  *Node[T]
	tail  *Node[T]
	count int
}

func (l *LinkedList[T]) Front() *Node[T] {
	return l.root
}

func (l *LinkedList[T]) Back() *Node[T] {
	return l.tail
}

func (l *LinkedList[T]) Count() int {
	return l.count
}

func (l *LinkedList[T]) GetAt(idx int) *Node[T] {
	if idx >= l.Count() {
		return nil
	}
	i := 0
	for node := l.root; node != nil; node = node.next {
		if i == idx {
			return node
		}
		i++
	}
	return nil
}

func (l *LinkedList[T]) PushBack(val T) {
	node := &Node[T]{
		Value: val,
	}
	if l.tail == nil {
		l.root = node
		l.tail = node
		l.count = 1
		return
	}
	l.tail.next = node
	node.prev = l.tail
	l.tail = node
	l.count++
}

func (l *LinkedList[T]) PushFront(val T) {
	node := &Node[T]{
		Value: val,
	}
	if l.root == nil {
		l.root = node
		l.tail = node
		l.count = 1
		return
	}
	l.root.prev = node
	node.next = l.root
	l.root = node
	l.count++

}

func (l *LinkedList[T]) InsertAfter(node *Node[T], val T) {
	if !l.isIncluded(node) {
		return
	}

	n := &Node[T]{
		Value: val,
	}
	nextNode := node.next
	node.next = n

	n.next = nextNode
	n.prev = node

	if nextNode != nil {
		nextNode.prev = n
	}
	if node == l.tail {
		l.tail = n
	}
	l.count++
}
func (l *LinkedList[T]) isIncluded(node *Node[T]) bool {
	inner := l.root
	for ; inner != nil; inner = inner.next {
		if inner == node {
			return true
		}
	}
	return false
}

func (l *LinkedList[T]) InsertBefore(node *Node[T], val T) {
	if !l.isIncluded(node) {
		return
	}
	n := &Node[T]{
		Value: val,
	}
	prevNode := node.prev
	node.prev = n

	n.next = node
	n.prev = prevNode

	if prevNode != nil {
		prevNode.next = n
	}
	if node == l.root {
		l.root = n
	}
	l.count++

}

func (l *LinkedList[T]) PopFront() *Node[T] {
	// 맨 앞에 뺄 게 없으니
	if l.root == nil {
		return nil
	}
	// 기록
	n := l.root
	l.root = n.next
	if l.root != nil {
		l.root.prev = nil
	} else {
		l.tail = nil
	}
	n.next = nil
	l.count--
	return n
	// node := l.root
	// node.next = l.root
	// node.prev = nil
}

func (l *LinkedList[T]) Reverse() {
	if l.root == nil {
		return
	}
	node := l.root
	// 링크가 바뀌니 기억하고 있다가
	var next *Node[T]

	for node != nil {
		next = node.next

		node.prev, node.next = node.next, node.prev
		node = next
	}
	l.root, l.tail = l.tail, l.root
}

func (l *LinkedList[T]) PopBack() *Node[T] {
	if l.tail == nil {
		return nil
	}
	n := l.tail
	l.tail = n.prev
	if l.tail != nil {
		l.tail.next = nil
	} else {
		l.root = nil
	}
	n.prev = nil
	l.count--
	return n
}

func main() {

}