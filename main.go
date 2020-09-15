package main

import (
	"net/http"
	"html/template"
)

type get_form struct {
	username string
	password string
}

func main() {
	tmpl := template.Must(template.ParseFiles("index.html"))
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			tmpl.Execute(w, nil)
			return
		}
		det := get_form{
			username: r.FormValue("username"),
			password: r.FormValue("password"),
		}
		_ = det
		tmpl.Execute(w, "welcome")
	})
	http.ListenAndServe(":8080", nil)
}
