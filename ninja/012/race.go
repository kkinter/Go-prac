package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	fmt.Println("CPUs:", runtime.NumCPU())
	fmt.Println("Goroutines:", runtime.NumGoroutine())

	counter := 0

	const gs = 100
	var wg sync.WaitGroup
	wg.Add(gs)

	for i := 0; i < gs; i++ {
		go func() {
			// counter 공유 변수 공유 변수를 로컬 변수 v 에 할당
			v := counter
			// time.Sleep(time.Second)
			// Gosched CPU를 다른 루틴에 양보
			runtime.Gosched()
			// 로컬 변수 증가
			v++
			// 로컬 변수 값을 공유변수에 쓰고
			counter = v
			// 작업이 끝남
			wg.Done()
		}()
		fmt.Println("Goroutines:", runtime.NumGoroutine())
	}
	wg.Wait()
	fmt.Println("Goroutines:", runtime.NumGoroutine())
	fmt.Println("count:", counter)
}
