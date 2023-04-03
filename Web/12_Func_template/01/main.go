package main

import (
	"log"
	"os"
	"strings"
	"text/template"
)

var tpl *template.Template

type sage struct {
	Name  string
	Motto string
}

type car struct {
	Manufacturer string
	Model        string
	Doors        int
}

// type FuncMap map[string]any
/*
key string 이고 value 가  빈 인터페이스인 맵
빈 인터페이스란 메서드가 없는 인터페이스로
최소한 모든 타입에 메서드가 없어야 합니다
즉, 모든 타입이 빈 인터페이스여야 합니다
*/
// create a FuncMap to register functions.
// "uc" is what the func will be called in the template
// "uc" is the ToUpper func from package strings
// "ft" is a func I declared
// "ft" slices a string, returning the first three characters
var fm = template.FuncMap{
	// 데이터 구조 및 타입에 대한 값들
	"uc": strings.ToUpper, // key string 이고 value 가 함수
	"ft": firstThree, // 위와 동일
}

func init() {
	/* 
	func (r receiver)  (identifier(parameter)) (return)          
	func (t *Template) Funcs(funcMap FuncMap) *Template
	FuncMap 타입의 값
	*/
	tpl = template.Must(template.New("").Funcs(fm).ParseFiles("tpl.gohtml"))
	/*
	tpl = template.Must(template.ParseFiles("tpl.gohtml"))
	tpl = tpl.Funcs(fm)
	>>> panic: template: tpl.gohtml:10: function "uc" not defined
	우선 템플릿에 대한 포인터와 프로그램에 Funcs가 있다고 먼저 말한 다음
	파싱을 수행해야 합니다 Funcs가 파싱 이전에 있어야 해요
	프로그램에 Funcs가 있다고 먼저 말한 다음
	파싱을 수행해야 합니다 Funcs가 파싱 이전에 있어야 해요
	func New(name string) *Template
	*/
	
}

func firstThree(s string) string {
	s = strings.TrimSpace(s)
	if len(s) >= 3 {
		s = s[:3]
	}
	return s
}

func main() {

	b := sage{
		Name:  "Buddha",
		Motto: "The belief of no beliefs",
	}

	g := sage{
		Name:  "Gandhi",
		Motto: "Be the change",
	}

	m := sage{
		Name:  "Martin Luther King",
		Motto: "Hatred never ceases with hatred but with love alone is healed.",
	}

	f := car{
		Manufacturer: "Ford",
		Model:        "F150",
		Doors:        2,
	}

	c := car{
		Manufacturer: "Toyota",
		Model:        "Corolla",
		Doors:        4,
	}

	sages := []sage{b, g, m}
	cars := []car{f, c}

	data := struct {
		Wisdom    []sage
		Transport []car
	}{
		sages,
		cars,
	}

	err := tpl.ExecuteTemplate(os.Stdout, "tpl.gohtml", data)
	if err != nil {
		log.Fatalln(err)
	}
}