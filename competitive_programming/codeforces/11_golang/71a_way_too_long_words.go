package main

import "fmt"

func wayTooLong(word string) string {
	if len(word) <= 10 {
		return word
	}
	return fmt.Sprintf("%c%d%c", word[0], len(word)-2, word[len(word)-1])
}

func main() {
	if wayTooLong("word") != "word" || wayTooLong("localization") != "l10n" || wayTooLong("internationalization") != "i18n" {
		panic("way too long failed")
	}
	fmt.Println("71A way too long words ok")
}
