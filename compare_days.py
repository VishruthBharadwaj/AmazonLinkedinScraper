
import datetime
print('Please type in how many days it should be delivered to you like 4,5,6 etc..')
ip = int(input('Enter the no: '))
Previous_Date = datetime.datetime.today() + datetime.timedelta(days=ip)
dt = Previous_Date.date()
print(dt)
