package main

import (
	"context"
	"fmt"
	"time"
)
func main() {

    // create a background context
    ctx := context.Background()

    // create a new context with a timeout
    // that will cancel the context after 10ms
    // equivalent to:
    //         context.WithDeadline(ctx,
    //         time.Now().Add(10 *time.Millisecond))

    ctx, cancel := context.WithTimeout(ctx, 10*time.Millisecond)
    defer cancel()

    fmt.Println(ctx)
}