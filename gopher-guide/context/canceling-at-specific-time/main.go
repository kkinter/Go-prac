package main

import (
	"context"
	"fmt"
	"time"
)
func main() {

    // create a background context
    ctx := context.Background()

    // create an absolute date/time (January 1, 2030)
    deadline := time.Date(2030, 1, 1, 0, 0, 0, 0, time.UTC)
    fmt.Println("deadline:", deadline.Format(time.RFC3339))

    // create a new context with a deadline
    // that will cancel at January 1, 2030 00:00:00.
    ctx, cancel := context.WithDeadline(ctx, deadline)
    defer cancel()

    print(ctx)
}