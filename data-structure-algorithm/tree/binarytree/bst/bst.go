package bst

import "prac/data-structure-algorithm/tree/nodeinterface"

// 서로를 비교할 수 있는
type Lesser interface {
	Less(other Lesser) bool
}

type Tree struct {
	Root *TreeNode
}
type TreeNode struct {
	Value Lesser

	Left  *TreeNode
	Right *TreeNode
}

func (t *TreeNode) GetChilds() []nodeinterface.Node {
	var childs []nodeinterface.Node
	if t.Left == nil {
		childs = append(childs, nil)
	} else {
		childs = append(childs, t.Left)
	}

	if t.Right == nil {
		childs = append(childs, nil)
	} else {
		childs = append(childs, t.Right)
	}
	return childs
}

func (t *TreeNode) GetValue() any {
	return t.Value
}

func (t *Tree) Add(value Lesser) *TreeNode{
	if t.Root == nil {
		t.Root = &TreeNode{
			Value: value,
		}
		return t.Root
	}

	return t.Root.add(value)

}

func (t *TreeNode) add(value Lesser) *TreeNode {
	if t.Value.Less(value) {
		// 비어 있는 경우
		if t.Left == nil {
			t.Left = &TreeNode{
				Value: value,
			}
			return t.Left
		}
		return t.Left.add(value)
	} else {
		// 비어 있는 경우
		if t.Right == nil {
			t.Left = &TreeNode{
				Value: value,
			}
			return t.Right
		}
		return t.Right.add(value)
	}
}