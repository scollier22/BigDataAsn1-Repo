units_sold = float(input("Enter number of units sold: "))
unit_cost = float(input("Enter selling price per unit: "))

#caluculated revenue:

revenue = round(units_sold * unit_cost,2)

print("Number of units sold entered:", units_sold)
print("Selling price per unit entered:", unit_cost)
print("Total Revenue:", revenue)
