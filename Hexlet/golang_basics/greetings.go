package pkg

import (
		"fmt"
		"strings"
)

// Реализуйте функцию Greetings(name string) string, которая вернет строку-приветствие. 
// Например, при передаче имени Иван, возвращается Привет, Иван!. 
// Учтите, что имя может быть написано в разном регистре и содержать пробелы.

func Greetings(name string) string {
		name = strings.Trim(name, " ")
		name = strings.ToLower(name)
		name = strings.Title(name) //nolint

		return fmt.Sprintf("Привет, %s!", name)
}
