# A program to display a number of seconds in other units

data = 75475984

changedData = data

years = 0
days = 0
hours = 0
minutes = 0
seconds = 0
now = 0

if data == 0:
    now = 1
for i in range(100):
    if changedData >= 31556952:
        years += 1
        changedData -= 31556952

for i in range(365):
    if changedData >= 86400:
        days += 1
        changedData -= 86400

for i in range(24):
    if changedData >= 3600:
        hours += 1
        changedData -= 3600

for i in range(60):
    if changedData >= 60:
        minutes += 1
        changedData -= 60

for i in range(60):
    if changedData >= 1:
        seconds += 1
        changedData -= 1


if years or days or hours or minutes or seconds >= 1:
    print("Years: " + str(years) + "\nDays: " + str(days) + "\nHours: " + str(hours) + "\nMinutes: " + str(minutes) +
          "\nSeconds: " + str(seconds))
elif now == 1:
    print("Now!")
else:
    print("Something Went Wrong")
