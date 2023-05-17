
años=False
años=int(input('Gimme a year to calculate the number of seconds of that year.'))

if años%4 ==0:
    print(años,'is a leap year.\nTher\'re ',60.0**2.0*24.0*366.0,' seconds.')
elif not años > 0:
   print("Please input a positive number starting with one")
    
else:
  print(años,'is a non-leap year.\nTher\'re ',60.0**2.0*24.0*365.0,' seconds.')

'''
This is the replit answer

days_this_year = int(input("How many days are in this year?"))
days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute
if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
else:
  print("Number of seconds in a year are", result)
'''