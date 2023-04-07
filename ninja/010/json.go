package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	First string
	Last  string
	Age   int
}

func main() {
	p1 := Person{
		First: "James",
		Last:  "Bond",
		Age:   32,
	}

	p2 := Person{
		First: "Miss",
		Last:  "Moneypenny",
		Age:   34,
	}
	fmt.Println(p1)
	fmt.Println(p2)

	people := []Person{
		p1,
		p2,
	}

	fmt.Println(people)

	bs, err := json.Marshal(people)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(bs))

	var peopleUnmarshal []Person
	errUn := json.Unmarshal(bs, &peopleUnmarshal)
	if errUn != nil {
		fmt.Println("error:" , errUn)
	}
	fmt.Printf("%v\n", peopleUnmarshal)
	fmt.Printf("%+v\n", peopleUnmarshal)
	for k, v := range peopleUnmarshal{
		fmt.Println(k)
		fmt.Println(v.First, v.Age, v.Last)
	}
}