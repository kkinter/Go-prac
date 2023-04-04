package main

// https://www.acmicpc.net/problem/2935
import "fmt"

func main() {
    var A, B int64
    var op string

    fmt.Scanf("%d\n", &A)
    fmt.Scanf("%s\n", &op)
    fmt.Scanf("%d\n", &B)

    fmt.Println(A, B, op)
}