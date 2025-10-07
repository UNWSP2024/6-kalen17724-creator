# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program



def county_sales_tax(total_sales):
    county_tax = (total_sales/100) * 2.5   
    return county_tax 

def state_sales_tax(total_sales):
    state_tax = (total_sales/100) * 5 
    return state_tax 

def main():
   total_sales = float(input("Enter the total sales for the month: $"))

   county_tax = county_sales_tax(total_sales)
   state_tax = state_sales_tax(total_sales)
   total_tax = county_tax+state_tax 
   
   print (f"Your total sales is: ${total_sales:.2f}")
   
   print (f"Your total county sales tax is: ${county_tax:.2f}")
   print (f"Your total state sales tax is: ${state_tax:.2f}")
   print (f"Your total sales tax is: ${total_tax:.2f}")
   print (f"Your total income this month after tax is ${total_sales-total_tax:.2f}")

main()



