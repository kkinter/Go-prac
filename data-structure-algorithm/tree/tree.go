package tree

import "prac/data-structure-algorithm/tree/nodeinterface"

type TreeNode[T any] struct {
	Value T

	Childs []*TreeNode[T]
}

func (t *TreeNode[T]) GetChilds() []nodeinterface.Node {
	// 타입이 다르니 GetValue() 와 다르다
	// 트리 노드 포인터 타입의 슬라이스고
	// 반환해야하는 건 노드 인터페이스의 슬라이스 타입
	var childs []nodeinterface.Node
	for _, c := range t.Childs {
		childs = append(childs, c)
	}
	return childs
}

func (t *TreeNode[T]) GetValue() any {
	return t.Value
}

func (t *TreeNode[T]) Add(val T) *TreeNode[T] {
	n := &TreeNode[T]{
		Value: val,
	}
	t.Childs = append(t.Childs, n)
	return n
}

func (t *TreeNode[T]) Preorder(fn func(val T)) {
	if t == nil {
		return
	}
	// 현재 노드의 값을 매개변수로 받은 함수(fn)로 전달하여 처리하는 코드입니다.
	// 이는 현재 노드의 값을 방문(visit)하는 코드입니다.
	fn(t.Value)

	for _, n := range t.Childs {
		n.Preorder(fn)
	}
}

func (t *TreeNode[T]) DFS(fn func(val T)) {
	stack := []*TreeNode[T]{}
	stack = append(stack, t)

	for len(stack) > 0 {
		last := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		fn(last.Value)

		stack = append(stack, last.Childs...)

	}
}

func (t *TreeNode[T]) Postorder(fn func(val T)) {
	if t == nil {
		return
	}

	for _, n := range t.Childs {
		n.Postorder(fn)
	}
	fn(t.Value)
}

func (t *TreeNode[T]) BFS(fn func(val T)) {
	// que에 넣고 빼는 방식
	queue := make([]*TreeNode[T], 0)
	// 현재 노드를 큐에 넣는다
	queue = append(queue, t)

	for len(queue) > 0 {
		// pop
		front := queue[0]
		queue = queue[1:]

		// 빼온 노드를 순회
		fn(front.Value)

		// 뺴온 프론트의 자식을 que 에 넣는다
		queue = append(queue, front.Childs...)

	}
}