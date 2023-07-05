package pkg


import (
		"strings"
		"unicode"
		"fmt"
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


// Реализуйте функцию, которая генерирует предложение, подставляя переданные данные в возвращаемую строку.
// Например:
// GenerateSelfStory("Vlad", 25, 10.00000025) // "Hello! My name is Vlad. I'm 25 y.o. And I also have $10.00 in my wallet right now."
// Шаблон возвращаемой строки:
// Hello! My name is [name]. I'm [age] y.o. And I also have $[money with precision 2] in my wallet right now.
func GenerateSelfStory(name string, age int, money float64) string {
		return fmt.Sprintf("Hello! My name is %s. I'm %d y.o. And I also have $%.2f in my wallet right now.", name, age, money)
}
