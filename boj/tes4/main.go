package main

import (
	"fmt"
	"strconv"
)

func main() {
	 // 문자열을 정수로 변환하기
    numStr := "123"
    num, err := strconv.Atoi(numStr)
    if err != nil {
        // 변환 실패시 처리할 작업
        fmt.Println("변환 실패")
    } else {
        fmt.Println(num) // 123
    }
}