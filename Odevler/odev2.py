while True:
    list = []
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))
    date_of_birth = int(input("Enter your birthdate(just year): "))

    list.append(name)
    list.append(surname)
    list.append(age)
    list.append(date_of_birth)

    for i in list[2:3]:

        if age < 18:
            print("\nYou can't go out because it's too dangerous.\n")
        else:
            print("\nYou can go out to the street.\n")