package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	fmt.Println("CPUs", runtime.NumCPU())
	fmt.Println("Gors", runtime.NumGoroutine())

	// 공유 변수
	counter := 0
	// 고루틴 생성
	const gs = 100
	var wg sync.WaitGroup

	wg.Add(gs)

	for i := 0; i < gs; i++{
		go func ()  {
			v := counter
			runtime.Gosched()
			v++
			counter = v
			fmt.Println(counter)
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("end val", counter)
}