# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered

from datetime import datetime, timedelta

date_now = datetime.now()
print(date_now)

#timedelta is used for dates other than today
new_date = timedelta(days=1)
day_yesterday = date_now - new_date
print("Yesterday was: ", str(day_yesterday))

user_day = input("Please enter a date (dd/mm/yyyy): ")
user_day = datetime.strptime(user_day, '%d/%m/%Y')
print(str(user_day))

new_user_day = timedelta(weeks=1)
week_yesterday = user_day + new_user_day
print("Last week was: ", str(week_yesterday))
