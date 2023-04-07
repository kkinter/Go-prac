// package main

// import (
// 	"context"
// 	"fmt"
// )

// func main() {

// 	// create a new background context
// 	ctx := context.Background()

// 	// wrap the context with a new context
// 	// that has the key "A" and the value "a",
// 	ctx = context.WithValue(ctx, CtxKey("A"), "a")

// 	// wrap the context with a new context
// 	// that has the key "B" and the value "b",
// 	ctx = context.WithValue(ctx, CtxKey("B"), "b")

// 	// wrap the context with a new context
// 	// that has the key "C" and the value "c",
// 	ctx = context.WithValue(ctx, CtxKey("C"), "c")

// 	// print the final context
// 	print("ctx", ctx)

// 	// retrieve and print the value
// 	// for the key "A"
// 	a := ctx.Value(CtxKey("A"))
// 	fmt.Println("A:", a)

// 	// retrieve and print the value
// 	// for the key "B"
// 	b := ctx.Value(CtxKey("B"))
// 	fmt.Println("B:", b)

// 	// retrieve and print the value
// 	// for the key "C"
// 	c := ctx.Value(CtxKey("C"))
// 	fmt.Println("C:", c)

// }