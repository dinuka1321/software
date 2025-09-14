def main():
    airports = {}
    choice = ""

    while choice != "3":
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Your choice: ")

        if choice == "1":
            icao = input("Enter ICAO code: ").upper()
            name = input("Enter airport name: ")

            if icao in airports:
                print(f"Airport with ICAO code {icao} already exists: {airports[icao]}")
            else:
                airports[icao] = name
                print(f"Airport {name} added with ICAO code {icao}.")

        elif choice == "2":
            icao = input("Enter ICAO code to fetch: ").upper()

            if icao in airports:
                print(f"Airport name: {airports[icao]}")
            else:
                print(f"No airport found with ICAO code {icao}.")

        elif choice == "3":
            print("Exiting program. Goodbye!")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()