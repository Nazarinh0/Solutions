package pkg

import (
	"encoding/json"
	"errors"
)

// Для выполнения этого задания потребуется функция json.Unmarshal, которая декодирует JSON байты в структуру:

// package main

// import (
//     "encoding/json"
//     "fmt"
// )

// type HelloWorld struct {
//     Hello string
// }

// func main() {
//     hw := HelloWorld{}

//   // первым аргументом передается JSON-строка в виде слайса байт. Вторым аргументом указатель на структуру, в которую нужно декодировать результат.
//     err := json.Unmarshal([]byte("{\"hello\":\"world\"}"), &hw)

//     fmt.Printf("error: %s, struct: %+v\n", err, hw) // error: %!s(<nil>), struct: {Hello:world}
// }
// В API методах часто используются запросы с телом в виде JSON. 
// Такие тела нужно декодировать в структуры и валидировать. 
// Хоть это и не лучшая практика делать функции, в которых происходит несколько действий, 
// но для простоты примера реализуйте функцию, которая декодирует тело запроса из JSON в структуру CreateUserRequest и валидирует ее. 
// Если приходит невалидный JSON или структура заполнена неверно, функция должна вернуть ошибку.

// Структура запроса:

type CreateUserRequest struct {
    Email                string `json:"email"`
    Password             string `json:"password"`
    PasswordConfirmation string `json:"password_confirmation"`
}
// Список ошибок, которые нужно возвращать из функции:

// validation errors
var (
    ErrEmailRequired                = errors.New("email is required") // когда поле email не заполнено
    ErrPasswordRequired             = errors.New("password is required") // когда поле password не заполнено
    ErrPasswordConfirmationRequired = errors.New("password confirmation is required") // когда поле password_confirmation не заполнено
    ErrPasswordDoesNotMatch         = errors.New("password does not match with the confirmation") // когда поля password и password_confirmation не совпадают
)
// Примеры работы функции DecodeAndValidateRequest:

// DecodeAndValidateRequest([]byte("{\"email\":\"\",\"password\":\"test\",\"password_confirmation\":\"test\"}")) // CreateUserRequest{}, "email is required"
// DecodeAndValidateRequest([]byte("{\"email\":\"test\",\"password\":\"\",\"password_confirmation\":\"test\"}")) // CreateUserRequest{}, "password is required"
// DecodeAndValidateRequest([]byte("{\"email\":\"test\",\"password\":\"test\",\"password_confirmation\":\"\"}")) // CreateUserRequest{}, "password confirmation is required"
// DecodeAndValidateRequest([]byte("{\"email\":\"test\",\"password\":\"test\",\"password_confirmation\":\"test2\"}")) // CreateUserRequest{}, "password does not match with the confirmation"
// DecodeAndValidateRequest([]byte("{\"email\":\"email@test.com\",\"password\":\"passwordtest\",\"password_confirmation\":\"passwordtest\"}")) // CreateUserRequest{Email:"email@test.com", Password:"passwordtest", PasswordConfirmation:"passwordtest"}, nil

func DecodeAndValidateRequest(requestBody []byte) (CreateUserRequest, error) {
        r := CreateUserRequest{}
        err := json.Unmarshal(requestBody, &r)
        if r.Email == "" {
                return CreateUserRequest{}, ErrEmailRequired
        }
        if r.Password == "" {
                return CreateUserRequest{}, ErrPasswordRequired
        }
        if r.PasswordConfirmation == "" {
                return CreateUserRequest{}, ErrPasswordConfirmationRequired
        }
        if r.Password != r. PasswordConfirmation {
                return CreateUserRequest{}, ErrPasswordDoesNotMatch
        }
        return r, err

}


func DecodeAndValidateRequest2(requestBody []byte) (CreateUserRequest, error) {
		req := CreateUserRequest{}

		err := json.Unmarshal(requestBody, &req)
		if err != nil {
				return CreateUserRequest{}, err
		}

		err = validateCreateUserRequest(req)
		if err != nil {
				return CreateUserRequest{}, err
		}

		return req, nil
}

func validateCreateUserRequest(req CreateUserRequest) error {
		if req.Email == "" {
				return ErrEmailRequired
		}

		if req.Password == "" {
				return ErrPasswordRequired
		}

		if req.PasswordConfirmation == "" {
				return ErrPasswordConfirmationRequired
		}

		if req.Password != req.PasswordConfirmation {
				return ErrPasswordDoesNotMatch
		}

		return nil
}




// Какая-то функция возвращает критичные и некритичные ошибки:

// // некритичная ошибка валидации
type NonCriticalError struct{}

func (e NonCriticalError) Error() string {
    return "validation error"
}
 
// // критичные ошибки
var (
    ErrBadConnection = errors.New("bad connection")
    ErrBadRequest    = errors.New("bad request")
)
// Реализуйте функцию, которая возвращает текст ошибки, если она критичная. 
// Если ошибка некритичная, то возвращается пустая строка. 
// В случае неизвестной ошибки возвращается строка unknown error:

// GetErrorMsg(errors.New("bad connection")) // "bad connection"
// GetErrorMsg(errors.New("bad request")) // "bad request"
// GetErrorMsg(NonCriticalError{}) // ""
// GetErrorMsg(errors.New("random error")) // "unknown error"
const UnknownErrorMsg = "unknown error"

func GetErrorMsg(err error) string {
	if errors.As(err, &NonCriticalError{}) {
			return ""
	}
	if errors.Is(err, ErrBadConnection) {
				return ErrBadConnection.Error()
	}
	if errors.Is(err, ErrBadRequest) {
				return ErrBadRequest.Error()
	}
	return UnknownErrorMsg

}

var criticalErrs = []error{ErrBadRequest, ErrBadConnection}

// GetErrorMsg returns the err message if the error is critical. Otherwise it returns an empty string.
func GetErrorMsg2(err error) string {
		for _, crErr := range criticalErrs {
				if errors.Is(err, crErr) {
						return crErr.Error()
				}
		}

		if errors.As(err, &NonCriticalError{}) {
				return ""
		}

		return UnknownErrorMsg
}
