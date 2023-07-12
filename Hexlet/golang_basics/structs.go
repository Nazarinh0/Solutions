package pkg

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
						Val:  curr.Val,
				}
				curr = curr.Next
		}

		return r
}
