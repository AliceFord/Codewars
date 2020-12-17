import datetime

def dateAfter(date, amountOfDays):
    date_format = "%d/%m/%Y"
    date = datetime.datetime.strptime(date, date_format)
    date -= datetime.timedelta(days=amountOfDays)
    return datetime.datetime.strftime(date, date_format)

def daysBetween(date1, date2):
    date_format = "%d/%m/%Y"
    date1 = datetime.datetime.strptime(date1, date_format)
    date2 = datetime.datetime.strptime(date2, date_format)
    return (date2 - date1).days


# date1 = input("Input first date: ")
# date2 = input("Input second date: ")
# print(f"{daysBetween(date1, date2)} days")
date = input("Input date (e.g. 01/01/1970): ")
days = int(input("Input days after time: "))
print(dateAfter(days, date))