debt = float(input("Enter you debt here > "))
apr = float(input("Enter the APR here > "))
years = int(input("How many years will you be repaying the loan? > "))

for j in range(years):
  debt += debt*apr
  print("Year",j+1,"is", round(debt,2))
