package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Print("Please Provide the File to read")
	}
	_fil, _err := os.Open(os.Args[1])
	if _err != nil {
		return
	}
	var b []byte = []byte{' '}
	var answer int
	f := -1
	var temp [2]byte
	var count int = 1
	for count > 0 {
		_, err := _fil.Read(b)
		if b[0] >= '0' && b[0] <= '9' {
			if f < 1 {
				f++
			}
			temp[f] = b[0] - '0'
		}
		if b[0] == '\n' {
			answer += int(temp[0]*10 + temp[f])
			f = -1
		}
		if err != nil{
			answer += int(temp[0]*10 + temp[f])
			break
		}
	}
	print("The Answer is ",answer,"\n")
}
