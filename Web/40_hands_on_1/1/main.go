package main

import (
	"html/template"
	"net/http"
)

var tpl *template.Template

func init() {
	tpl = template.Must(template.ParseGlob("*.gohtml"))
}
type hotdog int

func (d hotdog) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// io.WriteString(w, "dog dog dog")
	var data string = "This is hotdog"
	tpl.ExecuteTemplate(w, "dog.gohtml", data)
}

type hotcat int

func (c hotcat) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// io.WriteString(w, "goestoeleven")
	var data string = "This is me"
	tpl.ExecuteTemplate(w, "me.gohtml", data)
}

func main() {
	var c hotcat
	var d hotdog

	http.Handle("/me", c)
	http.Handle("/dog", d)

	

	http.ListenAndServe(":8080", nil)
}