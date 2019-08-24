import datetime
now = datetime.datetime.now()
print("current date and time is :",now)
print("in y:m:d h:m:s format : " )
print(now.strftime("%Y-%m-%d  %H:%M:%S "))