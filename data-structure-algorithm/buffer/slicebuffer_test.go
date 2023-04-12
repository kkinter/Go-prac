package buffer

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestWrite(t *testing.T) {
	buf := NewSliceBuffer[byte]()

	buf.Write([]byte{1, 2, 3, 4}) // 일반적으로 네트워크를 통해서 데이터가 들어올 때, 바이트로 들어옴

	assert.Equal(t, 4, buf.Readable()) // 아직 안 읽은 데이터가 얼만큼인가를 반환하는 함수

}

func TestRead(t *testing.T) {
	buf := NewSliceBuffer[byte]()
	buf.Write([]byte{1, 2, 3, 4})
	assert.Equal(t, 4, buf.Readable())

	readedData := buf.Read(4)
	for i := 0; i < 4; i++{
		assert.Equal(t, byte(i+1), readedData[i])
	}

	assert.Equal(t, 0, buf.Readable())
	
}

func TestWriteAndRead(t *testing.T){
	buf := NewSliceBuffer[byte]()
	buf.Write([]byte{1, 2, 3, 4})
	assert.Equal(t, 4, buf.Readable())

	buf.Write([]byte{5, 6})
	assert.Equal(t, 6, buf.Readable())

	readedData := buf.Read(4)
	for i := 0; i < 4; i++{
		assert.Equal(t, byte(i+1), readedData[i])
	}

	assert.Equal(t, 2, buf.Readable())

	buf.Write([]byte{7, 8, 9})
	assert.Equal(t, 5, buf.Readable())

	readedData = buf.Read(4)
	for i := 0; i < 4; i++{
		assert.Equal(t, byte(i+5), readedData[i])
	}
	assert.Equal(t, 1, buf.Readable())
}