
// Реализуйте функцию, которая преобразует каждый элемент слайса strs с помощью функции mapFunc и возвращает новый слайс. 
// Учтите, что исходный слайс, который передается как strs, не должен измениться в процессе выполнения.

package pkg

// BEGIN (write your solution here)
func Map1(strs []string, mapFunc func(string) string) []string {
	        result := make([]string, len(strs))
	        for i := 0; i < len(strs); i++ {
	                	result[i] = mapFunc(strs[i])
	        }
	        return result
}


func Map2(strs [string], mapFunc func(string) string) []string {
		mapped := make([]string, len(strs))
		for i, s := range strs {
				mapped[i] = mapFunc(s)
		}

		return mapped
}
