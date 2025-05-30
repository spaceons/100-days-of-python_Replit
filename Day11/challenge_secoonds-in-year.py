days_this_year = int(input("Ile dni jest w tym roku? > "))

secondsInMinute = 60
minutesInHour = 60
hoursInDay = 24
leapYear = 366
year = 365

yearResults = secondsInMinute * minutesInHour * hoursInDay * year
leapYear_results = secondsInMinute * minutesInHour * hoursInDay * leapYear

if days_this_year == 366:
   print("Number of seconds in a leap year are", leapYear_results)
else:
  print("Number of seconds in a year are", yearResults)
