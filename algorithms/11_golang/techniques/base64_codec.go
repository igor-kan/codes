// Base64 encoding.
package main

import (
	"fmt"
	"strings"
)

const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

func encode(data []byte) string {
	var out strings.Builder
	for i := 0; i < len(data); i += 3 {
		v := uint(data[i]) << 16
		rem := len(data) - i
		if rem > 1 {
			v |= uint(data[i+1]) << 8
		}
		if rem > 2 {
			v |= uint(data[i+2])
		}
		out.WriteByte(alphabet[(v>>18)&63])
		out.WriteByte(alphabet[(v>>12)&63])
		if rem > 1 {
			out.WriteByte(alphabet[(v>>6)&63])
		} else {
			out.WriteByte('=')
		}
		if rem > 2 {
			out.WriteByte(alphabet[v&63])
		} else {
			out.WriteByte('=')
		}
	}
	return out.String()
}

func main() {
	if encode([]byte("foobar")) != "Zm9vYmFy" || encode([]byte("f")) != "Zg==" {
		panic("bad base64")
	}
	fmt.Println("base64 ok")
}
