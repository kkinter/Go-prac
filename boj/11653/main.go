// 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
package main

import "fmt"

func main() {
	var n int
	
	fmt.Scanln(&n)
	
	d := 2
	for n >= 2{
		if n % d == 0{
			fmt.Println(d)
			n = n / d
		} else {
			d++
		}
	}
}