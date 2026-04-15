from rental_system import RentalSystem, MaxHeap, heap_sort_cds

def main():
    system = RentalSystem()

    system.add_cd("Where are you? On Ho Yi")
    system.add_cd("RGP Side")
    system.add_cd("Ghost Slayer")
    system.add_cd("Destroyer")
    system.add_cd("spoker-man")
    system.add_cd("Dark Hallway")
    system.add_cd("No.8 exit")
    system.add_cd("My name is Jeff!")
    system.add_cd("Lonely Lonely Christmas")
    system.add_cd("Rush B")
    system.add_cd("On your mark! Set! BI!!")
    system.add_cd("Evolution")
    system.add_cd("The Growth")
    system.add_customer("Low presence's man - On Ho Yi")
    system.add_customer("Jeff")
    system.add_customer("Willian")
    system.add_customer("Basketball King - Li")

    while True:
        print("\n" + "="*50)
        print("   Movie CD Rental System")
        print("="*50)
        print("1. View all Movie CDs")
        print("2. View available Movie CDs")
        print("3. Borrow a Movie CD")
        print("4. Return a Movie CD")
        print("5. View customer's borrowed list")
        print("6. Add new Movie CD")
        print("7. Add new customer")
        print("8. View most popular CDs")
        print("9. Sort CDs by popularity")
        print("10. Exit")
        print("="*50)

        choice = input("Enter option (1-10): ").strip()

        if choice == "1":
            system.list_all_cds()
        elif choice == "2":
            system.get_available_cds()
        elif choice == "3":
            cust_id = input("Enter Customer ID (e.g. C1): ").strip()
            try:
                cd_id = int(input("Enter Movie CD ID (e.g. 101): "))
                system.borrow(cust_id, cd_id)
            except:
                print("Invalid input format")
        elif choice == "4":
            cust_id = input("Enter Customer ID: ").strip()
            try:
                cd_id = int(input("Enter Movie CD ID: "))
                system.return_cd(cust_id, cd_id)
            except:
                print("Invalid input format")
        elif choice == "5":
            cust_id = input("Enter Customer ID: ").strip()
            customer = system.get_customer(cust_id)
            if customer:
                print(f"\n{customer.name}'s borrowed records:")
                print(customer.get_borrowed_list())
            else:
                print("Customer does not exist")
        elif choice == "6":
            title = input("Movie title: ").strip()
            if title:
                system.add_cd(title)
            else:
                print("Movie title cannot be empty")
        elif choice == "7":
            name = input("Customer name: ").strip()
            if name:
                system.add_customer(name)
            else:
                print("Name cannot be empty")
        elif choice == "8":
            print("\n=== Most Popular CDs ===")
            heap = MaxHeap()
            for cd in system._cds:
                heap.insert(cd)
            top_cds = heap.get_top_n(3)
            if top_cds:
                for cd in top_cds:
                    print(cd.get_details())
            else:
                print("No CDs yet")
        elif choice == "9":
            print("\n=== Sorted by Popularity ===")
            sorted_cds = heap_sort_cds(system._cds)
            for cd in sorted_cds:
                print(cd.get_details())
        elif choice == "10":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()
