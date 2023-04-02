package main

import "fmt"

type person struct {
	first string
	last  string
}

type sercretAgent struct {
	person
	ltk bool
}

// 키워드 식별자 타입
// spaek 메소드가 붙은 모든 타입은 type human 이기도 하다
type human interface {
	speak()
}

// assertion 
func bar(h human){
	switch h.(type) {
	case person:
		fmt.Println("I was passed into barrrrr", h.(person).first)
	case sercretAgent:
		fmt.Println("I was passed into barrrrr", h.(sercretAgent).first)
	}
	fmt.Println("I was passed into bar", h)
}

// func (r receiver) identifier(parameter) (return(s)) { code...}

func (s sercretAgent) speak() {
	fmt.Println("I am", s.first, s.last, "- the agent speak")
}

func (p person) speak() {
	fmt.Println("I am", p.first, p.last, "- the person speak")
}

type hotdog int

func main() {
	sa1 := sercretAgent{
		person: person{
			first: "James",
			last:  "Bond",
		},
		ltk: true,
	}

	sa2 := sercretAgent{
		person: person{
			first: "Miss",
			last:  "Moneypenny",
		},
		ltk: true,
	}

	p1 := person{
		first: "Dr. ",
		last: "Yes",
	}

	fmt.Println(sa1)
	sa1.speak()
	sa2.speak()

	// bar
	bar(sa1)
	bar(sa2)

	fmt.Println(p1)
	
	p1.speak()
	bar(p1)

	// conversion (전환)
	var x hotdog = 42
	fmt.Println(x)
	fmt.Printf("%T\n", x)
	var y int
	y = int(x)
	fmt.Println(y)
	fmt.Printf("%T\n", y)


}
