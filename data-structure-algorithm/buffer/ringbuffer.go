package buffer

type RingBuffer[T any] struct {
	buf     []T
	readPt  int
	writePt int
	isFull  bool
}

func NewRingBuffer[T any](size int) *RingBuffer[T] {
	return &RingBuffer[T]{
		buf: make([]T, size),
	}
}

func (r *RingBuffer[T]) Write(data []T) int {
	// 데이터가 없거나 쓸 공간이 없는 경우, 0을 반환합니다.
	if len(data) == 0 || r.Writable() == 0 {
		return 0
	}

	var writed int
	// 버퍼의 writePt가 readPt보다 큰 경우, 버퍼의 끝부터 쓸 수 있는 공간을 계산합니다.
	if r.writePt >= r.readPt {
		writableToEnd := len(r.buf) - r.writePt
		// 쓸 수 있는 공간과 입력받은 데이터 중 작은 값을 실제로 쓸 데이터의 길이로 정합니다.
		writed = min(writableToEnd, len(data))
	} else { // 버퍼의 writePt가 readPt보다 작은 경우, 현재 writePt부터 버퍼의 끝까지 쓸 수 있는 공간을 계산합니다.
		writed = min(r.Writable(), len(data))
	}

	// 실제로 쓸 데이터의 길이만큼 버퍼에 복사합니다.
	copy(r.buf[r.writePt:], data[:writed])
	// writePt를 실제로 쓴 데이터의 길이만큼 증가시킵니다.
	r.writePt += writed
	// writePt가 버퍼의 길이보다 큰 경우, 처음부터 다시 쓰기 시작하도록 writePt를 버퍼의 길이로 나눈 나머지를 할당합니다.
	r.writePt %= len(r.buf)

	// 버퍼가 가득 찼는지 확인하고, 가득 찼다면 isFull 변수를 true로 설정합니다.
	if writed > 0 && r.writePt == r.readPt {
		r.isFull = true
	}

	// 입력받은 데이터 중에서 실제로 쓰인 데이터의 길이만큼을 반환합니다.
	remain := len(data) - writed
	if remain > 0 && r.Writable() > 0 {
		writed += r.Write(data[writed:])
	}

	return writed
}

func (r *RingBuffer[T]) Readable() int {
	if r.isFull {
		return len(r.buf)
	}
	if r.writePt < r.readPt {
		return len(r.buf) - r.readPt + r.writePt
	}
	return r.writePt - r.readPt
}

func (r *RingBuffer[T]) Writable() int {
	return len(r.buf) - r.Readable()
}

func (r *RingBuffer[T]) Read(count int) []T {
	// 읽을 데이터가 없거나, 읽을 개수(count)가 0 이하인 경우, 빈 슬라이스를 반환합니다.
	if r.Readable() == 0 || count <= 0 {
		return []T{}
	}
	// 실제로 읽을 데이터의 개수를 계산합니다.
	readCnt := min(count, r.Readable())
	// 반환할 슬라이스를 생성합니다.
	rst := make([]T, readCnt)

	// 버퍼의 readPt와 읽을 데이터의 개수를 더한 값이 버퍼의 길이보다 큰 경우,
	// 읽을 데이터가 버퍼의 끝에서 끊어진 경우입니다.
	if r.readPt+readCnt >= len(r.buf) {
		// 읽을 데이터가 끊어진 부분부터 끝까지를 복사합니다.
		remainUntilEnd := len(r.buf) - r.readPt
		copy(rst, r.buf[r.readPt:])
		// readPt를 다시 0으로 초기화합니다.
		r.readPt = 0

		// 끊어진 부분 이후부터 읽을 데이터를 복사합니다.
		remain := readCnt - remainUntilEnd
		copy(rst[remainUntilEnd:], r.buf[:remain])
		// readPt를 다시 설정합니다.
		r.readPt += remain
	} else {
		// 읽을 데이터가 끊어지지 않은 경우, 버퍼에서 읽을 데이터를 복사합니다.
		copy(rst, r.buf[r.readPt:r.readPt+readCnt])
		// readPt를 읽은 데이터의 개수만큼 증가시킵니다.
		r.readPt += readCnt
	}
	// 버퍼가 가득 찬 상태에서 데이터를 읽었다면, isFull 변수를 false로 설정합니다.
	r.isFull = false
	// 읽은 데이터를 반환합니다.
	return rst
}