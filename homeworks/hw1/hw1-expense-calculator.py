#Personal Finace Calculator
#Student : Thanankorn Choonin 6730202203 Sec.831
#Date : 26/7/68
#Purpose : Calculate monthly budget and savings

#Program
monthly_income = float(input("What is your monthly income(THB)?:"))
rent_cost = float(input("What is your Monthly rent/houseing cost ? :"))
food_budget = int(input("What is your food budget monthly(THB)? :"))
transportion_cost = float(input("What is your Monthly transportation expenses?:"))
entertainment_budget = int(input("Monthly of Entertainment budget?:"))
emergency_fund_percent = float(input("Percentage to save for emegency(e.g.,10.5)? :"))
investment_percent = float(input("Percentage to invest(e.g.,15.0)? :"))

#Calculate
Total_Fixed_Expenses = (rent_cost + transportion_cost)
Total_Variable_Expenses = (food_budget + entertainment_budget)
Total_Expenses = (Total_Fixed_Expenses + Total_Variable_Expenses )
Remaining_Income = (monthly_income - Total_Expenses )                  #คำนวณค่าใช้จ่ายต่างๆ
Emergency_Fund_Amount = (monthly_income * (emergency_fund_percent / 100)  )
Investment_Amount = (monthly_income * ( investment_percent / 100))
Avaliable_for_Saving = (Remaining_Income - Emergency_Fund_Amount - Investment_Amount  )
Expense_Ratio = (Total_Expenses / monthly_income) * 100

#Print
print("===MONTHLY BUDGET REPORT===")
print("Income:",monthly_income,"THB")
print("Fixed Expenses:",Total_Fixed_Expenses,"THB")
print("Variable Expenses:",Total_Variable_Expenses,"THB")
print("Total Expenses:",Total_Expenses,"THB")
print("Remaining:",Remaining_Income,"THB")

print("===SAVINGS BREAKDOWN===")
print("Emergency Fund","(",emergency_fund_percent,"%",")" ,":", Emergency_Fund_Amount ,"THB" )
print("Investment","(",investment_percent,"%",")" ,":", Investment_Amount ,"THB" )
print("Avaliable for Savings:",Avaliable_for_Saving,"THB" )

print("===ANALYSIS===")
print("Expense Ratio : ",Expense_Ratio,"%")