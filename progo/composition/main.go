package main

import (
	"fmt"
	"prac/progo/composition/store"
)
func main() {
    rentals := []*store.RentalBoat {
        store.NewRentalBoat("Rubber Ring", 10, 1, false, false, "N/A", "N/A"),
        store.NewRentalBoat("Yacht", 50000, 5, true, true, "Bob", "Alice"),
        store.NewRentalBoat("Super Yacht", 100000, 15, true, true,
            "Dora", "Charlie"),
    }
    for _, r := range rentals {
        fmt.Println("Rental Boat:", r.Name, "Rental Price:", r.Price(0.2),
            "Captain:", r.Captain)
    }
}


// func main() {
//     rentals := []*store.RentalBoat {
//         store.NewRentalBoat("Rubber Ring", 10, 1, false, false),
//         store.NewRentalBoat("Yacht", 50000, 5, true, true),
//         store.NewRentalBoat("Super Yacht", 100000, 15, true, true),
//     }
//     for _, r := range rentals {
//         fmt.Println("Rental Boat:", r.Name, "Rental Price:", r.Price(0.2))
//     }
// }

// func main() {
//     boats := []*store.Boat {
//         store.NewBoat("Kayak", 275, 1, false),
//         store.NewBoat("Canoe", 400, 3, false),
//         store.NewBoat("Tender", 650.25, 2, true),
//     }
//     for _, b := range boats {
//         fmt.Println("Conventional:", b.Product.Name, "Direct:", b.Name)
//     }
// }

// func main() {
//     kayak := store.NewProduct("Kayak", "Watersports", 275)
//     lifejacket := &store.Product{ Name: "Lifejacket", Category:  "Watersports"}
//     for _, p := range []*store.Product { kayak, lifejacket} {
//         fmt.Println("Name:", p.Name, "Category:", p.Category, "Price:", p.Price(0.2))
//     }
// }