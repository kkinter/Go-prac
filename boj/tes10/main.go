package main

import "fmt"

func main() {
	fmt.Println(solution(40))
}

func solution(n int) int {
	res := 0
	for i := 1; i <= n; i++ {
		
		tmp := res
		for tmp > 0 {
			if tmp%3 == 0 {
				res++
				tmp /= 10
			}
            if tmp / 10 == 3 || tmp / 10 == 6 || tmp / 10 == 9{ 
                res ++
                tmp /= 10
            }
			tmp /= 10
		}
        res++
        fmt.Println(i, "일 때", res)
	}
	return res
}