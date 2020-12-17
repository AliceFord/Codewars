import datetime

def birthdayToDay(birthday):
    return datetime.datetime.strptime(birthday, '%B %d, %Y').strftime('%A')

birthday = input("Input your birthday (e.g. January 1, 1970):")
print(birthdayToDay(birthday))