# task 1

print ('Task 1: \n')
import datetime
today = datetime.datetime.now()
fdfromnow = today - datetime.timedelta(days = 5)
print(f"today is {today.strftime("%d.%m.%Y")} and five days ago was {fdfromnow.strftime("%d.%m.%Y")} \n")

# task 2

print ('Task 2: \n')
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)
print (f"yesterday was {yesterday.strftime("%d.%m.%Y")}, today is {today.strftime("%d.%m.%Y")}, tomorrow will be {tomorrow.strftime("%d.%m.%Y")} \n")

# task 3

print ('Task 3: \n')
def skoradrop(raw):
    return raw.replace(microsecond = 0)
today = datetime.datetime.now()
print (f"DATE TODAY IS I THINK... HMMM.. YEAH IT'S {skoradrop(today)} \n")

# task 4

print ('Task 4: \n')
day1 = datetime.datetime(2025, 2, 10, 12, 0)
day2 = datetime.datetime(2025, 2, 15, 12, 30)
difference = (day1 - day2)
print(f"seconds between two dates: {abs(difference.total_seconds())}")