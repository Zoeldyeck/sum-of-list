from operations import add, substract, multiply, divide
def get_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b
def main():
    while True:
        print("\nChoose the operation:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit") 
        choice = input("Enter your choice(1/2/3/4/5): ")
        if choice == '1':
            a, b = get_numbers()
            print(f"{a} + {b} = {add(a, b)}")
        elif choice == '2':
            a, b = get_numbers()
            print(f"{a} - {b} = {substract(a, b)}")
        elif choice == '3':
            a, b = get_numbers()
            print(f"{a} * {b} = {multiply(a, b)}")
        elif choice == '4':
            a, b = get_numbers()
            try:
                print(f"{a} / {b} = {divide(a, b)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")
if __name__ == "__main__":
    main()