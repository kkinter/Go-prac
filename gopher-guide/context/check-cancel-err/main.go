package main

import (
	"context"
	"fmt"
)
func main() {

    // create a background context
    ctx := context.Background()

    // wrap the context with a
    // cancellable context
    ctx, cancel := context.WithCancel(ctx)

    // check the error:
    //
    fmt.Println("ctx.Err()", ctx.Err())

    // cancel the context
    cancel()

    // check the error:
    // context.Canceled
    fmt.Println("ctx.Err()", ctx.Err())

    // check the error again:
    // context.Canceled
    fmt.Println("ctx.Err()", ctx.Err())
}