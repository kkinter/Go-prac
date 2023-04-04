package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    t, _ := strconv.Atoi(scanner.Text())
    
    for i := 0; i < t; i++ {
        scanner.Scan()
        args := strings.Fields(scanner.Text())
				fmt.Println("args :", args)
        x, _ := strconv.ParseFloat(args[0], 64)
        
        for j := 1; j < len(args); j++ {
            switch args[j] {
            case "@":
                x *= 3
            case "%":
                x += 5
            case "#":
                x -= 7
            }
        }
        fmt.Printf("%.2f\n", x)
    }
}