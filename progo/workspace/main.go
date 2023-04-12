package main

import (
	"fmt"
	// currencyFmt "prac/progo/workspace/packages/fmt"
	. "prac/progo/workspace/packages/fmt"
	"prac/progo/workspace/packages/store"
	"prac/progo/workspace/packages/store/cart"
)

func main() {
    product := store.NewProduct("Kayak", "Watersports", 279)
    cart := cart.Cart {
        CustomerName: "Alice",
        Products: []store.Product{ *product },
    }
    fmt.Println("Name:", cart.CustomerName)
    fmt.Println("Total:",  ToCurrency(cart.GetTotal()))


    // fmt.Println("Price:", currencyFmt.ToCurrency(product.Price()))
    // fmt.Println("Price:", ToCurrency(product.Price()))
}
 
