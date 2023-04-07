package main

import (
	"context"
	"fmt"
)

type CtxKey string

const (
    RequestID CtxKey = "request_id"
)

func WithBar(ctx context.Context) context.Context {
    // wrap the context with a request_id
    // to represent this specific bar request
    ctx = context.WithValue(ctx, RequestID, "456")

    // maliciously replace the request_id
    // set by foo
    ctx = context.WithValue(ctx, foo.RequestID, "???")

    // return the wrapped context
    return ctx
}

func main() {
    // create a background context
    ctx := context.Background()

    // wrap the context with foo
    ctx = foo.WithFoo(ctx)

    // wrap the context with bar
    ctx = bar.WithBar(ctx)

    // retrieve the foo.RequestID
    // value from the context
    id := ctx.Value(foo.RequestID)

    // print the value
    fmt.Println("foo.RequestID: ", id)
}

func WithFoo(ctx context.Context) context.Context {
    // wrap the context with a request_id
    // to represent this specific foo request
    ctx = context.WithValue(ctx, RequestID, "123")

    // return the wrapped context
    return ctx
}