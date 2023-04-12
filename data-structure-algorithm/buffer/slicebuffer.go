package buffer

type SliceBuffer[T any] struct {
	buf []T
}

func NewSliceBuffer[T any]() *SliceBuffer[T] {
	return &SliceBuffer[T]{}
}

func (s *SliceBuffer[T]) Write(data []T) {
	s.buf = append(s.buf, data...) // 데이터는 슬라이스
}

func (s *SliceBuffer[T]) Readable() int {
	return len(s.buf)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func (s *SliceBuffer[T]) Read(count int) []T {
	readCount := min(count, s.Readable())
	rst := make([]T, readCount)

	copy(rst, s.buf[:readCount])
	s.buf = s.buf[readCount:]
	return rst
}