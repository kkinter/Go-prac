package main

import "fmt"

func main() {
	sMap := map[string]int{}

	if v, ok := sMap["woo"]; ok {
		fmt.Println(v)
	} else{
        sMap["woo"] = 1
    }
    fmt.Println(sMap)
}