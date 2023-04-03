package main

import (
	"log"
	"os"
	"text/template"
)

func main() {
	// ParseFiles 는 템플릿에 대한 포인터와 오류를 반환
	// tpl 이 포인터
	// 포인터를 컨테이너로 여겨라 ?
	// 포인터가 파싱한 모든 템플릿을 보유하는 컨테이너 이기 떄문
	// func ParseFiles(filenames ...string) (*Template, error)
	// 포인터가 생기면 Execute 를 쓸 수 있음
	// func (t *Template) Execute(wr io.Writer, data any) error
	tpl, err := template.ParseFiles("tpl.gohtml")
	if err != nil {
		log.Fatalln(err)
	}
	// Execute 를 실행하면 writer 와 데이터가 생김
	// 이 경우엔 os.stdout 이 writer 고 데이터는 nil
	err = tpl.Execute(os.Stdout, nil)
	if err != nil{
		log.Fatalln(err)
	}
}