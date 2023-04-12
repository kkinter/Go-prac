package main

import "fmt"
type Product struct {
    name, category string
    price float64
}
func calcTax(product *Product) {
    if ((*product).price > 100) {
        (*product).price += (*product).price * 0.2
    }
}
func main() {
    kayak := Product {
        name: "Kayak",
        category: "Watersports",
        price: 275,
    }
    calcTax(&kayak)
    fmt.Println("Name:", kayak.name, "Category:",
        kayak.category, "Price", kayak.price)
}