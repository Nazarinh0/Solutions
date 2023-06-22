package pkg

// Реализуйте функцию, которая удаляет элемент по индексу i из слайса nums. 
// Если приходит несуществующий индекс, то из функции возвращается исходный слайс. 
// Порядок элементов может быть нарушен после удаления элемента.
func Remove1(nums []int, i int) []int {
		if i >= len(nums) || i < 0 {
				return nums
		}
		
		result := make([]int, 0, len(nums)-1)
		result = append(result, nums[:i]...)
		result = append(result, nums[i + 1:]...)
		return result
}


func Remove2(nums [] int, i int) []int {
		if i < 0 || i >= len(nums) {
				return nums
		}
		
		nums[i] = nums[len(nums) - 1]
		return nums[:len(nums) - 1]
}



// Реализуйте функцию, которая создает копию слайса src с длиной maxLen. 
// Если maxLen равен нулю или отрицательный, то функция возвращает пустой слайс []int{}. 
// Если maxLen больше длины src, то возвращается полная копия src.
func IntsCopy1(src []int, maxLen int) []int {
		cp := []int{}
		if maxLen <= 0 {
				return cp
		}

		if maxLen > len(src) {
			cp = make([]int, len(src))
			copy(cp, src)
		} else {
			cp = make([]int, maxLen)
			copy(cp, src)
		}

		return cp
}

func IntsCopy2(src []int, maxLen int) []int {
		if maxLen <= 0 {
				return []int{}
		}
		
		if maxLen > len(src) {
			maxLen = len(src)
		}

		cp := make([]int, maxLen)
		copy(cp, src)

		return cp

}


// Реализуйте функцию, которая возвращает отсортированный слайс, состоящий из уникальных идентификаторов userIDs. 
// Обработка должна происходить in-place, то есть без создания новых слайсов.
import "sort"

func UniqueSortedUserIDs1(userIDs []int64) []int64 {
	if len(userIDs) < 2 {
			return userIDs
	}

	sort.Slice(userIDs, func(i, j int) bool {
			return userIDs[i] < userIDs[j]
	})

	j := 0
	for i := 1; i < len(userIDs); i++ {
			if userIDs[j] == userIDs[i] {
					continue
			}
			j++
			userIDs[j] = userIDs[i]
	}
	return userIDs[:j+1]
}

func UniqueSortedUserIDs2(userIDs []int64) []int64 {
		if len(userIDs) < 2 {
				return userIDs
	}

		sort.SliceStable(userIDs, func(i, j int) bool { return userIDs[i] < userIDs[j] })
		uniqPointer := 0
		for i := 1; i < len(userIDs); i++ {
				if userIDs[uniqPointer] != userIDs[i] {
						uniqPointer++
						userIDs[uniqPointer] = userIDs[i]
				}
		}

		return userIDs[:uniqPointer+1]
}


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
