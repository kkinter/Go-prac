// 메인 고루틴 외에 두 개의 추가 고루틴을 실행합니다.
// 각각의 추가 고루틴은 무언가를 출력해야합니다.
// waitgroups를 사용하여 각 고루틴이 종료되기 전에 프로그램이 종료되도록합니다.

package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {
	go foo()
	go foo()
	wg.Add(2)
	bar()
	wg.Wait()
}

func foo(){
	fmt.Println("ran foo")
	wg.Done()
}

func bar(){
	fmt.Println("ran bar")
}