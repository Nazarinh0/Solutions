package pkg

import (
	"testing"
	"github.com/stretchr/testify/assert"
)
// Реализуйте функцию, которая возвращает слайс, состоящий из уникальных идентификаторов userIDs. 
// Порядок слайса должен сохраниться.
func UniqueUserIDs1(userIDs []int64) []int64 {
	uniqueIDs := make([]int64, 0, len(userIDs))
	seen := make(map[int64]bool)
	
	for _, id := range userIDs {
			if !seen[id] {
					uniqueIDs = append(uniqueIDs, id)
					seen[id] = true
			}
	}
return uniqueIDs
}

func UniqueUserIDs2(userIDs []int64) []int64 {
// пустая структура struct{} — это тип данных, который занимает 0 байт
// используется, когда нужно проверять в мапе только наличие ключа
	processed := make(map[int64]struct{})

	uniqUserIDs := make([]int64, 0)
	for _, uid := range userIDs {
			_, ok := processed[uid]
			if ok {
				continue
			}

			uniqUserIDs = append(uniqUserIDs, uid)
			processed[uid] = struct{}{}
	}

	return uniqUserIDs
}


// Реализуйте функцию, которая возвращает самое часто встречаемое слово в слайсе. 
// Если таких слов несколько, то возвращается первое из них.
func mostPopularWord(words []string) string {
		counter := make(map[string]int)

		for _, word := range words {
				counter[word]++
		}

		maxCount := 0
		topWord := ""

		for word, count := range counter {
				if count > maxCount {
						maxCount = count
						topWord = word
				}
		}

		return topWord
}

func TestMostPopularWord(t *testing.T) {
		a := assert.New(t)
		a.Equal("hello", mostPopularWord([]string{"hello", "world", "hello"}))
		a.Equal("world", mostPopularWord([]string{"hello", "world", "hello", "world", "world"}))
		a.Equal("one", mostPopularWord([]string{"one", "two", "three", "four", "five"}))
		a.Equal("c", mostPopularWord([]string{"a", "b", "c", "c", "d", "e", "e", "d"}))
		a.Equal("a", mostPopularWord([]string{"a", "c", "c", "a"}))
}

func MostPopularWord2(words []string) string {
	wordsCount := make(map[string]int, 0)
	mostPopWord := ""
	max := 0

	for i := len(words) - 1; i >= 0; i -= 1 {
		word := words[i]
		wordsCount[word] += 1
		if wordsCount[word] >= max {
			max = wordsCount[word]
			mostPopWord = word
		}
	}

	return mostPopWord
}