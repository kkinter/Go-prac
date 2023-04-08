package single

type Node[T any] struct {
	next  *Node[T]
	Value T
}

type LinkedList[T any] struct {
	root *Node[T] // 시작 노드
	tail *Node[T] // 마지막 노드

	count int
}

// tail 로 추가
func (l *LinkedList[T]) PushBack(value T) {
	node := &Node[T]{
		Value: value,
	}
	l.count++
	if l.root == nil {
		l.root = node
		l.tail = node
		return
	}
	// 노드가 있는 상황
	l.tail.next = node
	l.tail = node

}

func (l *LinkedList[T]) PushFront(value T) {
	node := &Node[T]{
		Value: value,
	}
	l.count++
	if l.root == nil {
		l.root = node
		l.tail = node
		return
	}
	node.next = l.root
	l.root = node
}

// 첫 번쨰 노드 반환
func (l *LinkedList[T]) Front() *Node[T] {
	return l.root
}

// 마지막 노드 반환
func (l *LinkedList[T]) Back() *Node[T] {
	return l.tail
}

// 루트 부터 세어야함
// O(n)
func (l *LinkedList[T]) Count() int {
	node := l.root
	cnt := 0

	for ; node != nil; node = node.next {
		cnt++
	}
	return cnt
}

// O(1)
// 상세한 구현이 필요, 다만 잘 해주면 더 빠르다
func (l *LinkedList[T]) Count2() int {
	return l.count
}

func (l *LinkedList[T]) GetAt(idx int) *Node[T] {
	if idx >= l.Count2() {
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

func (l *LinkedList[T]) InsertAfter(node *Node[T], value T) {
	if !l.isIncluded(node) {
		return
	}
	// 노드가 없을 때, count 가 추가됨
	newNode := &Node[T]{
		Value: value,
	}
	// origNext := node.next
	// node.next = newNode
	// newNode.next = origNext

	node.next, newNode.next = newNode, node.next
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

func (l *LinkedList[T]) InsertBefore(node *Node[T], value T) {
	// prevNode 함수 때문에 필요 없음
	// if !l.isIncluded(node) {
	// 	return
	// }
	// root 일 경우
	if node == l.root {
		l.PushFront(value)
		return
	}
	prevNode := l.findPrevNode(node)
	// 추가할 노드
	newNode := &Node[T]{
		Value: value,
	}
	// 이전 노드를 찾아서, root 부터 시작해서 찾아야 함

	prevNode.next, newNode.next = newNode, node
	l.count++
}

func (l *LinkedList[T]) findPrevNode(node *Node[T]) *Node[T] {
	inner := l.root
	for ; inner != nil; inner = inner.next {
		if inner.next == node {
			return inner
		}
	}
	return nil
}

// X 체크
func (l *LinkedList[T]) PopFront() {
	if l.root == nil {
		return
	}
	// l.root = l.root.next
	// l.root.next = nil
	l.root.next, l.root = nil, l.root.next
	l.count--
	if l.root == nil {
		l.tail = nil
	}
}

// 이전 노드를 찾아서 이전 노드의 넥스트를 다음 노드로 바꿔줘야 함.
func (l *LinkedList[T]) Remove(node *Node[T]) {
	if node == l.root {
		l.PopFront()
		return
	}
	// 루트도 없는데 이전노드가 없다는 노드가 리스트 안에 없다
	prev := l.findPrevNode(node)
	if prev == nil {
		return
	}

	prev.next = node.next
	node.next = nil
	/*
		그러니까 지금 테일이 마지막 거 없었을 때 테일이 갱신이 안 됐어요 자 이건 왜 그러냐면 우리가 지금
		리무브 했는데 여기서 만약에 내가 없애 노드가 테일이었으면
		갱신을 해줘야 되겠죠 만약에 노드가 마지막 노드를 없앤거였으면
		테일도 갱신을 해줘야 된다 프리비어스로 바꿔준다 마지막으로 오셨으니까 이전 노드가 테일이 되겠죠
		자 이렇게 했을 때 이렇게 하면 되는 거 알 수 있습니다 자 이렇게 해서 자 싱글 링크드 리스트
		를 만들어 봤습니다 시간이 많이 지난 관계로 더블링클 리스트는 다음 시간에 하도록
		하겠습니다네 감사합니다
	*/
	if node == l.tail {
		l.tail = prev
	}
	l.count--
}

func main() {

}