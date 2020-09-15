package main

import (
	"net/http"
	"html/template"
	"fmt"
)

type get_form struct {
	username string
	password string
}

func login(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		t, _  := template.ParseFiles("index.html")
		t.Execute(w, nil)
	} else {
		r.ParseForm()
		fmt.Println("username: ", r.Form["username"])
		fmt.Println("password: ", r.Form["password"])
	}
}

func main() {
	http.HandleFunc("/", login)
	http.ListenAndServe("192.168.1.7:8000", nil)
	//err := http.ListenAndServe(":8080", nil)
}
