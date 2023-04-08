package main

import (
	"context"
	"fmt"
	"time"
)


func main() {

    // create a background context
    ctx := context.Background()

    // wrap the context with the ability
    // to cancel it
    ctx, cancel := context.WithCancel(ctx)

    // defer cancellation of the context
    // to ensure that any resources are
    // cleaned up regardless of how the
    // function exits
    defer cancel()

    // create 5 listeners
    for i := 0; i < 5; i++ {

        // launch listener in a goroutine
        go listener(ctx, i)

    }

    // allow the listeners to start
    time.Sleep(time.Millisecond * 500)

    fmt.Println("canceling the context")

    // cancel the context and tell the
    // listeners to exit
    cancel()

    // allow the listeners to exit
    time.Sleep(time.Millisecond * 500)
}
func listener(ctx context.Context, i int) {
    fmt.Printf("listener %d is waiting\n", i)

    // this will block until the context
    // given context is canceled
    <-ctx.Done()

    fmt.Printf("listener %d is exiting\n", i)
}