package main

import (
	"context"
	"fmt"
)

// CtxKeyA is used to wrap keys
// associated with a A request
//      CtxKeyA("request_id")
//      CtxKeyA("user_id")
type CtxKeyA string

// CtxKeyB is used to wrap keys
// associated with a B request
//      CtxKeyB("request_id")
//      CtxKeyB("user_id")
type CtxKeyB string

func main() {
	// create a new background context
	ctx := context.Background()

	// call the A function
	// passing in the background context
	A(ctx)
}

func A(ctx context.Context) {
    // wrap the context with a request_id
    // to represent this specific A request
    key := CtxKeyA("request_id")
    ctx = context.WithValue(ctx, key, "123")

    // call B with the wrapped context
    B(ctx)
}

func B(ctx context.Context) {
    // wrap the context with a request_id
    // to represent this specific B request
    key := CtxKeyB("request_id")
    ctx = context.WithValue(ctx, key, "456")

    Logger(ctx)
}

// Logger logs the webs request_id
// as well as the request_id from the B
func Logger(ctx context.Context) {
    // retrieve the request_id from the A request
    aKey := CtxKeyA("request_id")
    aVal := ctx.Value(aKey)

    // print the request_id from the A request
    fmt.Println("A", aKey, aVal)

    // retrieve the request_id from the B request
    bKey := CtxKeyB("request_id")
    bVal := ctx.Value(bKey)

    // print the request_id from the B request
    fmt.Println("B", bKey, bVal)
}