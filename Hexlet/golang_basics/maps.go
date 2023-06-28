package pkg

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
