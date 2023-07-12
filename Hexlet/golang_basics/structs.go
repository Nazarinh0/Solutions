package pkg

// Одна из самых популярных структур в алгоритмическом программировании — это связный список (linked list).
// Эта структура используется как основа для стеков и очередей, графов, хранения связанных данных в больших количествах. 
// Реализуйте метод, который возвращает развернутый связный список. 
// Учтите, что исходный список не должен измениться.

// Пример:

// // ListNode is a node of a linked list.
// type ListNode struct {
//     Next *ListNode
//     Val  int
// }

// // связный список вида: 1 -> 2
// list := &ListNode{
//     Next: &ListNode{
//         Next: nil,
//         Val: 20,
//     },
//     Val: 10,
// }

// reversed := list.Reverse() // 2 -> 1

// fmt.Println(list) // 1 -> 2, то есть исходный список не изменился


type ListNode struct {
		Next *ListNode
		Val  int
}

func (head *ListNode) Reverse() *ListNode {
		if head == nil {
				return nil
		}

		var r *ListNode

		curr := head
		for curr != nil {
				r = &ListNode{
						Next: r,
						Val: curr.Val,
				}
				curr = curr.Next
		}

		return r
}


// Представим, что есть структура Person, содержащая возраст человека:
type Person struct {
    Age uint8
}
// Реализуйте тип PersonList (слайс структур Person), 
// с методом GetAgePopularity(), который возвращает мапу, где ключ — возраст, а значение — кол-во таких возрастов:

// pl := PersonList{
//   {Age: 18},
//   {Age: 44},
//   {Age: 18},
// }

// pl.GetAgePopularity() // map[18:2 44:1]
type PersonList []Person
func (p1 PersonList) GetAgePopularity() map[uint8]int {
        r := make(map[uint8]int)

        for _, v := range(p1) {
                r[v.Age]++
        }
        return r
}
