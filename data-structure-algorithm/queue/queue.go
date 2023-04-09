package queue

import "prac/data-structure-algorithm/doublelinkedlist"

type Queue[T any] struct {
	l *doublelinkedlist.LinkedList[T]
}

func New[T any]() *Queue[T] {
	return &Queue[T]{
		l: &doublelinkedlist.LinkedList[T]{},
	}
}

func (s *Queue[T]) Push(val T) {
	s.l.PushBack(val)
}

func (s *Queue[T]) Pop() T{
	return s.l.PopFront().Value
}