annual_salary = float(input("What is your annual Salary? "))
print("Annual Salary is ", annual_salary)
portion_saved = float(input("What is the portion saved in decimal? "))
print("Salary saved is ", annual_salary*portion_saved, " per year")
total_cost = float(input("What is the cost of your dream home? "))
r = 0.04
portion_down_payment = 0.25*total_cost
current_savings = 0
months = 0
while(current_savings <= portion_down_payment):
	current_savings = current_savings + ((annual_salary/12)*portion_saved) + (0.04 * current_savings)/12
	months = months + 1

print("You need", months, "months to buy the dream house")
