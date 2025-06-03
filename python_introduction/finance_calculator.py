monthlyinc = int (input("Enter your monthly income:"))
monthlyexp = int(input("Enter your total monthly expenses:"))
monthlysav = monthlyinc - monthlyexp
print ("Your monthly savings are", monthlysav)
projectedsavings = monthlysav * 12 + (monthlysav * 12 * 0.05)
print ("Projected savings after one year, with interest, is:",projectedsavings)

