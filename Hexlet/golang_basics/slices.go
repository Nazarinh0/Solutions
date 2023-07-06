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


// Реализуйте функцию, которая принимает вариативный список слайсов чисел
// и объединяет их в 1, сохраняя последовательность:
// MergeNumberLists([]int{1, 2}, []int{3}, []int{4}) // [1, 2, 3, 4]
func MergeNumberLists(numberLists ...[]int) []int {
		res := make([]int, 0)
		for _, n := range numberLists {
				res = append(res, n...)
		}
		
		return res
}

func MergeNumberLists2(numberLists ...[]int) []int {
		mergedCap := 0
		for i := 0; i < len(numberLists); i++ {
			mergedCap += len(numberLists[i])
		}

		merged := make([]int, 0, mergedCap)
		for _, nl := range numberLists {
			merged = append(merged, nl...)
		}

		return merged
}