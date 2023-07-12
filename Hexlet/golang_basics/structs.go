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
