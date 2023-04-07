package main

import (
	"context"
	"fmt"
)

type ctx_id string

const (
    ID ctx_id = "id"
)

func main() {
    // create a background context
    bg := context.Background()
    
    // pass the background context to the A function
    A(bg)

    // pass the background context to the B function
    B(bg)
}

func A(ctx context.Context) {
    // wrap ctx with a new context
    // with the ID set to "A"
    A := context.WithValue(ctx, ID, "A")
    fmt.Println("A", A)

    // pass the A context to the A1 function
    A1(A)
}

func A1(ctx context.Context) {
    A1 := context.WithValue(ctx, ID, "A1")
    fmt.Println("A1", A1)
}

func B(ctx context.Context) {
    // wrap ctx with a new context
    // with the ID set to "B"
    B := context.WithValue(ctx, ID, "B")
    fmt.Println("B", B)

    // pass the B context to the B1 function
    B1(B)
}

func B1(ctx context.Context) {
    // wrap ctx with a new context
    // with the ID set to "B1"
    B1 := context.WithValue(ctx, ID, "B1")
    fmt.Println("B1", B1)

    // pass the B1 context to the B1a function
    B1a(B1)
}

func B1a(ctx context.Context) {
    // wrap ctx with a new context
    // with the ID set to "B1a"
    B1a := context.WithValue(ctx, ID, "B1a")
    fmt.Println("B1a", B1a)
}