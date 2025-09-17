#user is asked to input an integer 
entry = input("Enter an integer eg. 2 , 3, 5, ..... ")
match entry:
    case int():
        print(f"You entered an integer of value {entry}")
    case _:
        print(f"You entered the wrong data type of value {entry}")