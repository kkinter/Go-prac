package main

import (
	"context"
	"fmt"
)

type CtxKeyA string

type CtxKeyB string

const (
    // A_RequestID can be used to
    // retrieve the request_id for
    // the A request
    A_RequestID CtxKeyA = "request_id"
    // A_SESSION_ID CtxKeyA = "session_id"
    // A_SERVER_ID CtxKeyA = "server_id"
    // other keys...

    // B_RequestID can be used to
    // retrieve the request_id for
    // the B request
    B_RequestID CtxKeyB = "request_id"
)

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
    aKey := A_RequestID
    aVal := ctx.Value(aKey)

    // print the request_id from the A request
    fmt.Println("A", aKey, aVal)

    // retrieve the request_id from the B request
    bKey := B_RequestID
    bVal := ctx.Value(bKey)

    // print the request_id from the B request
    fmt.Println("B", bKey, bVal)
}