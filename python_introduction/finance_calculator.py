monthly_income = input("Enter your monthly income:") #requesting user monthly income
monthly_expenses = input("Enter your total monthly expenses:") #requesting user monthly expenses
monthly_savings = int(monthly_income) - int(monthly_expenses) #calculating monthly savings of user
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are", f"${monthly_savings}")
print("Projected savings after one year, with interest, is: "f"${projected_savings}")
#work completed 