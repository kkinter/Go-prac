/*
프로그램의 성능 기준을 맞추기 위해 템플릿으로 할 수 있는
마지막 작업은 모든 템플릿을 한 번만 파싱했는지 확인
*/

package main

import (
	"log"
	"os"
	"text/template"
)

// 패키지 레벨 스코프
var tpl *template.Template 

// 프로그램 초기화 프로그램이 시작되면 실행
// func Must(t *Template, err error) *Template
func init() {
	tpl = template.Must(template.ParseGlob("templates/*"))
}

func main() {
	// templates 폴더에서 gmao 확장자를 가진 모든 파일을 파싱
	// tpl, err := template.ParseGlob("templates/*.gmao")

	// tpl, err := template.ParseGlob("templates/*")
	// if err != nil {
	// 	log.Fatalln(err)
	// }

	err := tpl.Execute(os.Stdout, nil)
	if err != nil {
		log.Fatalln(err)
	}

	err = tpl.ExecuteTemplate(os.Stdout, "vespa.gohtml", nil)
	if err != nil {
		log.Fatalln(err)
	}

	err = tpl.ExecuteTemplate(os.Stdout, "two.gohtml", nil)
	if err != nil {
		log.Fatalln(err)
	}

	err = tpl.ExecuteTemplate(os.Stdout, "one.gohtml", nil)
	if err != nil {
		log.Fatalln(err)
	}
}