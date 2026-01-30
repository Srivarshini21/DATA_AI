
from __future__ import annotations

def main() -> None:
    while True:
        print("\nWelcome to Uber App")
        print("1. Book a Ride")
        print("2. View Rides")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            from booking import book_ride

            book_ride()
        elif choice == "2":
            from view_rides import view_rides

            view_rides()
        elif choice == "3":
            print("Thank you for using Uber App!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()