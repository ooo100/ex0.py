Name = input("Name?")
Hourly_Wage = int(input("Hourly_wage?"))
Working_Hours = int(input("Working_hour?"))
OT_Hours = int(input("OT_Hours?"))
OT_Rate = 1.5
Total_Salary = (Hourly_Wage * Working_Hours) + (Hourly_Wage * OT_Rate * OT_Hours)
print(Name + "," + str(Total_Salary))
