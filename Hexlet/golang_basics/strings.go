package pkg


import (
		"strings"
		"unicode"
)


// Реализуйте функцию, которая принимает на вход состоящую из ASCII символов строку s
// и возвращает новую строку, где каждый символ из входящей строки сдвинут вперед на число step.

// Например:
// ShiftASCII("abc", 0) // "abc"
// ShiftASCII("abc1", 1) // "bcd2"
// ShiftASCII("bcd2", -1) // "abc1"
// ShiftASCII("hi", 10) // "rs"


func ShiftASCII(s string, step int) string {
		newStr := ""
		for _, b := range([]byte(s)) {
				newStr += string(b + byte(step))
		}
		return newStr
	}


func ShiftASCII2(s string, step int) string {
		if step == 0 {
				return s
		}

		shifted := make([]byte, len(s))
		for i := 0; i < len(s); i++ {
				shift := step + int(s[i])
				shifted[i] = byte(shift)
		}

		return string(shifted)
}


// Реализуйте функцию, которая возвращает true, если строка s состоит только из ASCII символов.
func IsASCII(s string) bool {
		for _, ch := range s {
				if ch > 127 {  // можно unicode.MaxASCII вместо 127
						return false
				}
		}
		return true
}


// Реализуйте функцию, которая возвращает только латинские символы из строки s.
// Например:
// LatinLetters("привет world!") // "world"
func LatinLetters1(s string) string {
	latin := strings.Builder{}
	for _, ch := range s {
			if unicode.Is(unicode.Latin, ch) {
					latin.WriteString(string(ch))
			}
	}
	return latin.String()
}

func LatinLetters2(s string) string {
	sb := &strings.Builder{}

	for _, r := range s {
		if unicode.Is(unicode.Latin, r) {
			sb.WriteRune(r)
		}
	}

	return sb.String()
}
