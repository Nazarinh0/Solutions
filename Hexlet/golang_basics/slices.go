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