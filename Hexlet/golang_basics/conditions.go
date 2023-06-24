package main

import (
		"fmt"
		"strings"
)

func statusByName(name string) string {
    // функция проверяет, что строка name начинается с подстроки "Mr."
    if strings.HasPrefix(name, "Mr.") {
        return "married man"
    } else if strings.HasPrefix(name, "Mrs.") {
        return "married woman"
    } else {
        return "single person"
    }
}

func main() {
    n := "Mr. Doe"
    fmt.Println(n + " is a " + statusByName(n)) // Mr. Doe is a married man

    n = "Mrs. Berry"
    fmt.Println(n + " is a " + statusByName(n)) // Mrs. Berry is a married woman

    n = "Karl"
    fmt.Println(n + " is a " + statusByName(n)) // Karl is a single person
}

// Реализуйте функцию, которая добавляет язык locale как поддомен к домену domain. 
// Язык может прийти пустым, тогда нужно добавить поддомен en.. 
// Например:
// DomainForLocale("site.com", "") // en.site.com
// DomainForLocale("site.com", "ru") // ru.site.com

func DomainForLocale(domain, locale string) string {
	if locale == "" {
		locale = "en"
	}

	return fmt.Sprintf("%s.%s", locale, domain)
}

// Реализуйте функцию, которая изменяет строку s в зависимости от переданного режима mode. 
// когда передается mode "dash", нужно заменить все пробелы на дефисы "-"
// ModifySpaces("hello world", "dash") // hello-world
// // когда передается mode "underscore", нужно заменить все пробелы на нижние подчеркивания "_"
// ModifySpaces("hello world", "underscore") // hello_world
// // когда передается неизвестный или пустой mode, заменяем все пробелы на звездочки "*"
// ModifySpaces("hello world", "unknown") // hello*world
// ModifySpaces("hello world", "") // hello*world

// Для замены символов в строке существует функция ReplaceAll(s, old, new string) string из пакета strings:
// strings.ReplaceAll("hello world!", "world!", "buddy!") // hello buddy!
// strings.ReplaceAll("one two three", " ", "_") // one_two_three

func ModifySpaces(s, mode string) string {
	var replacement string

	switch mode {
	case "dash":
		replacement = "-"
	case "underscore":
		replacement = "_"
	default:
		replacement = "*"
	}

	return strings.ReplaceAll(s, " ", replacement)
}

// Представим, что нам нужно написать конвертер ошибок в числовой формат для gRPC.
// Реализуйте функцию, которая возвращает числовой код для заданного значения. 
// Список сообщений и соответствующих кодов:
// OK = 0
// CANCELLED = 1
// UNKNOWN = 2

const (
	OkMsg        = "OK"
	CancelledMsg = "CANCELLED"
)

const (
	OkCode = iota
	CancelledCode
	UnknownCode
)

func ErrorMessageToCode(msg string) int {
	switch msg {
	case OkMsg:
		return OkCode
	case CancelledMsg:
		return CancelledCode
	}

	return UnknownCode
}
ErrorMessageToCode("CANCELLED")
