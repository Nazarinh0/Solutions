package pkg

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