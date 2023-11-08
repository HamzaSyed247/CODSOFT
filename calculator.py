def calculator():
    while True:
        n1 = int(input("Enter 1st number: "))
        n2 = int(input("Enter 2nd number: "))

        print("\n ********** CALCULATOR ***********")
        print("\n 1. ADDITION \n 2. SUBTRACTION \n 3. MULTIPLICATION \n 4. DIVISION")
        ch = input("Which Operation do you want to perform: ")

        if ch == '1':
            result = n1 + n2
            print("The sum of {} and {} is: {}".format(n1, n2, result))
        elif ch == '2':
            result = n1 - n2
            print("The Subtraction of {} and {} is: {}".format(n1, n2, result))
        elif ch == '3':
            result = n1 * n2
            print("The Multiplication of {} and {} is: {}".format(n1, n2, result))
        elif ch == '4':
            if n2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = n1 / n2
                print("The Division of {} and {} is: {}".format(n1, n2, result))
        else:
            print("Choose Correct Option")

        choice = input("Do you want to perform any other calculation? (yes/no): ")
        if choice != 'yes':
            break;

calculator()
