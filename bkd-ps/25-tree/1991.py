import sys
sys.stdin = open("input.txt")


def preorder(root, traverse):
    if root != '.':
        traverse.append(root)
        preorder(tree[root][0], traverse)
        preorder(tree[root][1], traverse)
    return traverse


def inorder(root, traverse):
    if root != '.':
        inorder(tree[root][0], traverse)
        traverse.append(root)
        inorder(tree[root][1], traverse)
    return traverse


def postorder(root, traverse):
    if root != '.':
        postorder(tree[root][0], traverse)
        postorder(tree[root][1], traverse)
        traverse.append(root)
    return traverse


n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

print(*preorder('A', []), sep='')
print(*inorder('A', []), sep='')
print(*postorder('A', []), sep='')
