package main

import (
	"fmt"
	//"os"
	"net/http"
	"io/ioutil"
	//"net"
		)

func return_handel(in http.ResponseWriter, o *http.Request) {
		return_file, _ := ioutil.ReadFile("index.html")
		fmt.Fprint(in, string(return_file))
}

func main() {
	http.HandleFunc("/", return_handel)
	http.ListenAndServe(":8000", nil)
}
