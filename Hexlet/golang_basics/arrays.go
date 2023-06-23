package pkg

// Реализуйтункцию, которая записывает значение val в массив nums по индексу i, если индекс находится в рамках массива. 
// В противном случае массив возвращается без изменения.
func SafeWrite(nums [5]int, i, val int) [5]int {
		if i >= 0 && i < len(nums) {
				nums[i] = val
		}

		return nums
}
