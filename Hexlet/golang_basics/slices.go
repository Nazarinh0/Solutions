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

