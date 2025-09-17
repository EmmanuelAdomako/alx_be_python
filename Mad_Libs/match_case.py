days = str(input("Enter a day (Monday - Sunday)")).lower()
match days:
    case "Monday":
        print("Happy Monday")
    case "Tuesday":
        print("Happy Tuesday")
    case _ :
        print("Invalid day")