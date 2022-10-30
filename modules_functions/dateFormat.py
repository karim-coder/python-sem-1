from datetime import datetime

date = datetime.now()

print("""
Q) Write a Python script to display the various Date Time formats.
  a) Current date and time
  b) Current year
  c) Month of year
  d) Week number of the year
  e) Weekday of the week
  f) Day of year
  g) Day of the month
  h) Day of week

Ans)  """)
print(" a) Current date and time = %s" % date)
print(" b) Current year = %s" % date.year)
print(" c) Current Month of %s = %s" % (date.year,  date.strftime("%B")))
print(" d) Week number of %s = %s" % (date.year, date.strftime("%V")))
print(" e) Weekday of current week = %s(%s)" % (date.strftime("%A"), date.weekday()+1))
print(" f) Current day of %s = %s" % (date.year, date.strftime("%j")))
print(" g) Current day of month %s = %s" % (date.year, date.strftime("%d")))
print(" h) Day of current week = %s" % date.strftime("%A"))