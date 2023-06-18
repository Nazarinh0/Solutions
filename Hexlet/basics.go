package pkg

import "strconv"
import "math"

// Converting int to string
func IntToString(num int) string {
  return strconv.Itoa(num)
}

// Getting minimum of two given number, math.Min takes float64 type
func MinInt(x, y int) int {
	res := math.Min(float64(x), float64(y))
	return int(res)
  }

// Checking if id is positive number and text isn't empty
func IsValid(id int, text string) bool {
	return id > 0 && text != ""
  }
  